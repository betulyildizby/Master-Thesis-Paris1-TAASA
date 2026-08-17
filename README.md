# Dynamic Customer Satisfaction Modeling via Trend-Aware Aspect Sentiment Alignment (T-AASA)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FAIR Principles](https://img.shields.io/badge/FAIR-Science--Compliant-green.svg)](https://www.go-fair.org/fair-principles/)

**Master Thesis Research Project**  
**Student:** Betül YILDIZ  
**Advisor:** Prof. Camille Salinesi  
**Institution:** Université Paris 1 Panthéon - Sorbonne (UFR 27 - Observatoire de l'IA)  

---

## 📌 Executive Summary

Traditional e-commerce product evaluation relies heavily on static historical average star ratings ($R_{\text{base}}$). However, static star averages suffer from severe **time-blindness** (treating 5-year-old reviews equally with recent feedback) and **trend-blindness** (ignoring active market feature demand and individual user priorities).

This repository contains the official implementation of **T-AASA (Trend-Aware Aspect Sentiment Alignment)** integrated with the **SDMAE (Syntax-Denoising Masked Autoencoder)** aspect sentiment analysis baseline. T-AASA introduces three dynamic components:
1. **Temporal Recency Decay ($e^{-\lambda \Delta t}$):** Weights recent customer feedback higher to track quality degradation over time.
2. **Market Trend Velocity ($T_k$):** Automatically detects rising market aspect trends over time ($\text{Velocity} > 1.03$).
3. **User Aspect Profiling ($W_{u,k}$):** Customizes product rankings based on individual buyer aspect priority matrices.

Empirical evaluation on 5,000 authentic Amazon Electronics reviews demonstrates that T-AASA yields a **+46.95% aspect satisfaction gain** for top recommendations and achieves a **90.0% ground-truth manual review alignment rate** (vs. 20.0% for static star averages).

---

## 📂 Repository Structure

```
.
├── experiment_code.py                 # Core T-AASA + SDMAE integration pipeline
├── run_statistical_tests.py           # Statistical hypothesis testing script (t-test, Wilcoxon)
├── getting_dataset.py                 # Dataset loader & preprocessor
├── SDMAE/                              # Baseline SDMAE neural network architecture
├── results/                           # Experimental evaluation logs & outputs
│   ├── Thesis_Methodology_and_Hypothesis_Report.md  # Detailed methodology & SEM hypotheses
│   ├── taasa_vs_sdmae_quantitative_metrics.csv      # Overall quantitative evaluation metrics
│   ├── manual_evaluation_comparison.csv             # Product ranking comparison table
│   ├── manual_review_dataset_mapping.csv            # Dataset row mappings & review texts
│   ├── detailed_predictions_250.csv                 # Step-by-step sample prediction breakdown
│   ├── taasa_sdmae_integrated_comparison.csv        # Product A-E baseline vs T-AASA scores
│   ├── taasa_sdmae_integrated_summary.txt           # Ranking divergence summary
│   └── statistical_hypothesis_tests.txt             # Statistical significance test logs (p < 0.001)
└── README.md                          # Repository documentation
```

---

## 🔬 Key Experimental Findings

### 📊 Quantitative Metrics Summary

| Evaluation Metric | Baseline SDMAE | Proposed T-AASA | Absolute Gain | **Relative Gain (%)** |
| :--- | :---: | :---: | :---: | :---: |
| **Top-1 Aspect Satisfaction Score** | `0.1621` | `0.2382` | `+0.0761` | **+%46.95** |
| **Top-2 Avg Aspect Satisfaction** | `0.1643` | `0.2190` | `+0.0548` | **+%33.32** |
| **Ground-Truth Review Alignment Rate** | `20.0%` | `90.0%` | `+70.0%` | **+%350.0** |
| **Rank Reordering Rate** | `0.0%` | `100.0%` | `+100.0%` | **100% Dynamic Reordering** |

### 📈 Statistical Significance (Hypothesis Testing)
* **Hypothesis 1 (H1 - Score Alteration):** Paired t-test $t = 10.2189$, $p = 1.066 \times 10^{-20}$ ($p < 0.001$); Wilcoxon signed-rank test $W = 4952.5$, $p = 6.625 \times 10^{-21}$ ($p < 0.001$). **Null Hypothesis $H_{1,0}$ REJECTED**.
* **Hypothesis 2 (H2 - Satisfaction Gain):** T-AASA achieves statistically superior aspect satisfaction (+46.95% gain). **Null Hypothesis $H_{2,0}$ REJECTED**.

---

## 🚀 Quick Start & Reproduction

### Prerequisites
* Python 3.8+
* PyTorch 1.10+
* NumPy, Pandas, SciPy

### Running the Integrated Experiment
```bash
python experiment_code.py
```

### Running Statistical Hypothesis Tests
```bash
python run_statistical_tests.py
```

---

## 📄 License & FAIR Science Compliance

This repository is shared in accordance with **FAIR (Findable, Accessible, Interoperable, Reusable)** open science guidelines for master thesis evaluation at Université Paris 1 Panthéon - Sorbonne.

For inquiries, please contact: **Betül YILDIZ** (Université Paris 1 Panthéon - Sorbonne).
