import rasterio
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the DEM file
dem_path = "dem.tif"

with rasterio.open(dem_path) as src:
    dem = src.read(1).astype(float)
    nodata = src.nodatavals[0]
    transform = src.transform
    bounds = src.bounds

    # Mask NoData values
    if nodata is not None:
        dem[dem == nodata] = np.nan

# 2. Convert Pixel Resolution from Degrees to Meters
res_x_deg = abs(transform[0])
res_y_deg = abs(transform[4])

# Center latitude of the tile
lat_center = (bounds.bottom + bounds.top) / 2.0

# 1 degree latitude ~ 111,320 meters
pixel_size_y = res_y_deg * 111320
pixel_size_x = res_x_deg * 111320 * np.cos(np.radians(lat_center))

# 3. Compute Basic Morphometric / Relief Parameters
elevation_min = np.nanmin(dem)
elevation_max = np.nanmax(dem)
elevation_mean = np.nanmean(dem)
total_relief = elevation_max - elevation_min

# Hypsometric Integral (HI) approximation
hypsometric_integral = (elevation_mean - elevation_min) / total_relief

# 4. Calculate Slope (in degrees)
dy, dx = np.gradient(dem)
slope_rad = np.arctan(np.sqrt((dx / pixel_size_x)**2 + (dy / pixel_size_y)**2))
slope_deg = np.degrees(slope_rad)

# 5. Print Summary Report to Console
print("=" * 45)
print("     HYDRO-MORPHOMETRIC SUMMARY REPORT     ")
print("=" * 45)
print(f"Minimum Elevation : {elevation_min:.2f} m")
print(f"Maximum Elevation : {elevation_max:.2f} m")
print(f"Mean Elevation    : {elevation_mean:.2f} m")
print(f"Total Relief      : {total_relief:.2f} m")
print(f"Hypsometric Int.  : {hypsometric_integral:.3f}")
print(f"Average Slope     : {np.nanmean(slope_deg):.2f}°")
print("=" * 45)

# 6. Plot Elevation and Slope Maps
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Elevation Plot
im1 = ax[0].imshow(dem, cmap='terrain')
ax[0].set_title("Elevation Profile (m)", fontsize=12, fontweight='bold')
fig.colorbar(im1, ax=ax[0], shrink=0.7, label='Elevation (m)')
ax[0].axis('off')

# Slope Plot
im2 = ax[1].imshow(slope_deg, cmap='inferno')
ax[1].set_title("Terrain Slope (°)", fontsize=12, fontweight='bold')
fig.colorbar(im2, ax=ax[1], shrink=0.7, label='Slope (°)')
ax[1].axis('off')

plt.tight_layout()
plt.savefig("morphometry_summary.png", dpi=300, bbox_inches='tight')
plt.show()

# 7. Save Summary Report to Text File
report_text = f"""=============================================
     HYDRO-MORPHOMETRIC SUMMARY REPORT
=============================================
Minimum Elevation : {elevation_min:.2f} m
Maximum Elevation : {elevation_max:.2f} m
Mean Elevation    : {elevation_mean:.2f} m
Total Relief      : {total_relief:.2f} m
Hypsometric Int.  : {hypsometric_integral:.3f}
Average Slope     : {np.nanmean(slope_deg):.2f}°
=============================================
"""

with open("morphometry_report.txt", "w") as f:
    f.write(report_text)

print("\nReport successfully saved as 'morphometry_report.txt'!")