# Automated Watershed Hydro-Morphometric Analysis

An automated, lightweight Python workflow to perform quantitative hydro-geomorphometric analysis on satellite Digital Elevation Models (DEMs). Built using `rasterio`, `numpy`, and `matplotlib`, this script processes elevation rasters to evaluate surface relief, slope distribution, and watershed erosion maturity without relying on heavy desktop GIS engines.

---

## 💻 Tech Stack & Libraries
* **Language:** Python 3.x
* **Spatial Data Processing:** `rasterio`
* **Numerical Computation:** `numpy`
* **Visualization:** `matplotlib`

---

## 🛠️ Key Technical Features
* **Automated Spatial Ingestion:** Directly parses USGS SRTM 30m GeoTIFF rasters into 2D NumPy arrays.
* **Geographic CRS Correction:** Dynamically handles degree-to-meter unit mismatches using trigonometric latitudinal scaling ($\Delta x = \Delta x_{\text{deg}} \times 111,320 \times \cos(\phi)$) to prevent spatial slope distortion.
* **Slope Matrix Vectorization:** Uses central finite differences (`np.gradient`) to generate realistic 2D slope magnitude matrices.
* **Erosion Stage Classification:** Calculates the **Hypsometric Integral ($HI$)** to quantitatively determine watershed landscape maturity.
* **Automated Output:** Saves high-resolution (300 DPI) spatial maps and logs summary metrics to a text file.

---

## 📊 Summary Results

| Metric | Calculated Value | Hydrological Significance |
| :--- | :--- | :--- |
| **Elevation Range** | -28.00 m to 1596.00 m | Vertical energy baseline across catchment |
| **Total Relief ($R$)** | 1624.00 m | Vertical relief potential along escarpment ridges |
| **Hypsometric Integral ($HI$)** | **0.267** | $HI < 0.35$ classifies catchment in an "Old/Monadnock" erosion stage |
| **Average Slope** | **8.07°** | Stable baseline concentration time across low-lying valleys |

---

## 🖼️ Spatial Outputs

![Elevation and Slope Profile](morphometry_summary.png)

---

## 🚀 How to Run

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Hydro-Morphometry-Analysis.git](https://github.com/AryanADRamteke/Hydro-Morphometry-Analysis.git)
   cd Hydro-Morphometry-Analysis
