---

# 📊 Univariate Exploratory Data Analysis (EDA)

![EDA Visualization Example](https://miro.medium.com/max/1400/1*4G__SV580CxFj78o9yUXuQ.png)

This repository contains a comprehensive univariate analysis of dataset features, focusing on understanding the distribution, central tendency, dispersion, and potential outliers in individual numerical variables.

---

## 🔍 Parameters Analyzed

For each numerical column in the dataset, the following statistical metrics are calculated:

| Parameter                     | Description                              | Formula / Interpretation          |
| ----------------------------- | ---------------------------------------- | --------------------------------- |
| **Mean**                      | Average of values                        | `sum(values) / n`                 |
| **Median**                    | Middle value (50th percentile)           | Robust to outliers                |
| **Mode**                      | Most frequent value                      | Value with highest frequency      |
| **Minimum / Maximum**         | Lowest and highest values                | Range boundaries                  |
| **Quartiles (Q1, Q2, Q3)**    | 25%, 50%, and 75% percentiles            | Q1 = 25%, Q2 = Median, Q3 = 75%   |
| **Interquartile Range (IQR)** | Spread of the middle 50%                 | `IQR = Q3 - Q1`                   |
| **1.5×IQR Rule**              | Outlier detection threshold              | `[Q1 - 1.5×IQR, Q3 + 1.5×IQR]`    |
| **Skewness**                  | Measure of asymmetry                     | >0: Right-skewed, <0: Left-skewed |
| **Kurtosis**                  | Measure of tail heaviness                | >3: Heavy tails, <3: Light tails  |
| **Variance**                  | Dispersion from the mean (squared units) | `sum((x - μ)²) / n`               |
| **Standard Deviation**        | Spread of values (original units)        | `√Variance`                       |

Additional concepts covered:

* **Normal Distribution**
* **Z-Score**
* **Probability Density Function (PDF)**

---

## 📁 Repository Structure

```
📂 Univariate_EDA/
├── 📄 Univariate Class and Function.py        # Core analysis class and functions
├── 📄 Placement.csv                           # Primary dataset
├── 📓 Central Tendency Univariate.ipynb       # Notebook on central tendency metrics
├── 📓 Placement Data Univariate Analysis.ipynb# Full univariate EDA notebook
├── 📓 Normal Distribution & PDF.ipynb         # PDF and Z-score exploration
└── 📄 README.md                                # Project documentation
```

---

## 🛠️ How to Use

```python
from univariate_analysis import UnivariateAnalyzer

analyzer = UnivariateAnalyzer(dataset)
results = analyzer.get_descriptive_stats()
```

This will return a dictionary of descriptive statistics for all numerical columns.

---

## 📌 Notes

* Ensure all required libraries (e.g., `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`) are installed.
* The code is modular and designed for easy reuse in different datasets.
* Perfect for beginners and intermediates working on data science, ML preprocessing, or academic EDA projects.

---

## 📬 Contact

For questions or contributions, feel free to open an issue or pull request!

---

