# THESIS METHODOLOGY, CONCEPTUAL SCOPE, AND HYPOTHESIS TESTING REPORT
**Project Title:** Dynamic Customer Satisfaction Modeling via Trend-Aware Aspect Sentiment Alignment (T-AASA) Integrated with SDMAE Baseline  
**Student:** Betül YILDIZ  
**Advisor:** Prof. Camille Salinesi (Université Paris 1 Panthéon - Sorbonne)  
**Document Purpose:** Supporting Documentation for Thesis Chapter 1, 3, 4 & 5 (Uploaded to Google Drive Repository)

---

## 📌 SECTION 1: TERMINOLOGY BOUNDARIES & CONCEPTUAL SCOPE

To ensure scientific rigor and prevent conceptual ambiguity, this work strictly delineates three distinct terminology boundaries:

```
====================================================================================================
CONCEPT TERMINOLOGY        DEFINITION & SCIENTIFIC SCOPE                     SCOPE BOUNDARY IN THIS WORK
====================================================================================================
1. SENTIMENT ANALYSIS      Extracting aspect-level polarity scores           [INCOMING INPUT / BASELINE]
                           from unstructured text (e.g., positive vs.       Performed by the underlying 
                           negative sentiment on 'battery' or 'sound').       SDMAE baseline neural network.

2. CUSTOMER SATISFACTION   Aggregating aspect sentiment, temporal decay,     [PRIMARY INNOVTION SCOPE]
   METRIC / MODEL          and market trend velocity into a dynamic,          The core contribution of 
                           time-aware satisfaction score per product.         this thesis (T-AASA Framework).

3. RECOMMENDATION SYSTEM   Applying collaborative filtering or content-       [DOWNSTREAM APPLICATION]
                           based filtering algorithms to generate user-       Serves as the evaluation context,
                           specific item recommendation lists.               outside core sentiment extraction.
====================================================================================================
```

---

## 🔬 SECTION 2: PROBLEM STATEMENT, ILLUSTATIVE EXAMPLE & PRIOR LITERATURE

### 2.1 The Problem Statement
Traditional e-commerce platforms evaluate products using historical average star ratings ($R_{\text{base}}$). However, static star averages suffer from two major flaws:
1. **Time Blindness:** They fail to distinguish between obsolete reviews written years ago and recent feedback.
2. **Trend & User Blindness:** They ignore active market feature trends and individual customer aspect preferences.

### 2.2 Concrete Illustrative Example (The Discrepancy Case)
Consider **Product_D** from our Amazon Electronics experimental dataset:
* **Legacy Star Rating:** **4.42 Stars** (Earned Rank #1 in traditional static baseline).
* **Historical Context:** Received hundreds of 5-star reviews between 2010 and 2018.
* **Recent Reality (2021 Feedback):** Recent customer reviews (e.g., CSV Line 3989) explicitly report battery degradation and overheating ($S_{\text{battery}} = 0.100$).
* **The Discrepancy:** Traditional star averages compute a high satisfaction value ($0.8848$), creating a severe discrepancy with *actual current customer satisfaction*.
* **T-AASA Solution:** By applying temporal recency decay ($e^{-\lambda \Delta t}$) and aspect alignment, T-AASA demotes Product_D to **Rank #3**, protecting buyers from purchasing degraded products.

### 2.3 Key Literature Citations
* **Rating Biases & Star Averages:** Resnick et al. (2000), Hu et al. (2006) - *Demonstrates how online star averages suffer from bimodal distribution and historical stagnation.*
* **Temporal Concept Drift & Recency Decay:** Koren (2009), Gama et al. (2014) - *Establishes the necessity of temporal decay models exp(-lambda * dt) in tracking customer preference drift.*
* **Aspect-Based Sentiment Analysis Baseline:** Tai et al. (2023) - *Provides the official SDMAE (Syntax-Denoising Masked Autoencoder) architecture for syntax-aware aspect sentiment extraction.*

---

## 🛠️ SECTION 3: THE METHOD - REUSABLE SCIENTIFIC RECIPE

The **T-AASA Method** is formulated as a domain-independent, reusable scientific recipe. Any researcher can re-apply this recipe to different domains (e.g., hotel reviews, mobile app feedback):

### Step 1: Aspect Sentiment Extraction with Temporal Recency Decay
For any review $r$ written at timestamp $t_r$, relative to reference evaluation timestamp $t_{\text{max}}$:
$$\Delta t = \frac{t_{\text{max}} - t_r}{\text{Seconds in Day}}$$
$$\text{Recency Weight}(t_r) = e^{-\lambda \cdot \Delta t} \quad (\lambda = 0.005)$$
$$S_{i,k}(t) = \frac{\sum_{r \in R_i} e^{-\lambda \Delta t} \cdot \text{Sentiment}(r, k)}{\sum_{r \in R_i} e^{-\lambda \Delta t}}$$

### Step 2: Market Trend Velocity Coefficient ($T_k$)
$$\text{Recent Rate}_k = \frac{\text{Mentions of aspect } k \text{ in recent window}}{\text{Total recent reviews}}$$
$$\text{Past Rate}_k = \frac{\text{Mentions of aspect } k \text{ in past window}}{\text{Total past reviews}}$$
$$\text{Velocity}_k = \frac{\text{Recent Rate}_k}{\text{Past Rate}_k + \epsilon}$$
$$T_k = \begin{cases} \min\left(2.0, \, 1.0 + (\text{Velocity}_k - 1.0) \times 1.5\right) & \text{if Velocity}_k > 1.03 \\ 1.0 & \text{otherwise} \end{cases}$$

### Step 3: User Aspect Preference Profiling ($W_{u,k}$)
Represent user $u$'s aspect priorities as a normalized vector $\mathbf{W}_u = [W_{u,1}, W_{u,2}, \dots, W_{u,K}]$, where $\sum_k W_{u,k} = 1.0$.

### Step 4: Fusion Engine Scoring Formula
$$\text{Score}_i = \alpha \cdot R_{\text{base}, i} + \beta \sum_{k} \left( W_{u,k} \cdot S_{i,k}(t) \cdot T_k \right) \quad (\alpha = 0.5, \beta = 0.5)$$

---

## 📊 SECTION 4: APPLICATION OF THE METHOD & DATA CHARACTERISTICS

### 4.1 Dataset Properties
* **Dataset:** Amazon Electronics Product Reviews Corpus.
* **Sample Size:** 5,000 authentic customer reviews with Unix timestamps spanning multi-year periods.
* **Target Product Groups:** 5 evaluated product subsets (Product_A to Product_E, 1,000 reviews per chunk).

### 4.2 Aspect Mention Frequencies & Trend Velocity
```
====================================================================================================
ASPECT CATEGORY    PAST MENTION RATE    RECENT MENTION RATE    VELOCITY (Vk)    TREND BOOSTER (Tk)
====================================================================================================
battery            18.65%               20.31%                 1.0893           1.134 (ACTIVE TREND)
sound              18.63%               15.28%                 0.8201           1.000 (NORMAL)
camera             15.17%               11.50%                 0.7580           1.000 (NORMAL)
screen              9.16%                8.82%                 0.9623           1.000 (NORMAL)
price              22.08%               16.69%                 0.7558           1.000 (NORMAL)
====================================================================================================
```

---

## 📈 SECTION 5: STRUCTURAL EQUATION MODEL & STATISTICAL HYPOTHESIS TESTING

### 5.1 Structural Variables Definition
* **Independent Variables (IVs):**
  1. $IV_1$: Algorithm Model Type (Static SDMAE Baseline vs. Dynamic T-AASA).
  2. $IV_2$: Review Recency Timestamp ($\Delta t$).
  3. $IV_3$: Market Aspect Trend Velocity ($T_k$).
  4. $IV_4$: User Aspect Importance Weights ($W_{u,k}$).
* **Dependent Variables (DVs):**
  1. $DV_1$: Final Recommendation Rank & Score ($\text{Score}_i$).
  2. $DV_2$: Customer Aspect Preference Satisfaction Score.
  3. $DV_3$: Ground-Truth Manual Review Alignment Rate.

### 5.2 Formal Hypotheses & Statistical Verification

#### **Hypothesis 1 (H1 - Score Alteration & Recency Shift):**
* **Null Hypothesis ($H_{1,0}$):** There is no significant difference between static SDMAE baseline scores and dynamic T-AASA scores ($DV_1$).
* **Alternative Hypothesis ($H_{1,1}$):** Dynamic recency decay and trend boosters cause a statistically significant deviation in recommendation scores.
* **Statistical Test Results:**
  * **Paired t-test t-statistic:** `10.2189`, **p-value:** `1.066e-20` ($p < 0.001$).
  * **Wilcoxon Signed-Rank W-statistic:** `4952.5`, **p-value:** `6.625e-21` ($p < 0.001$).
  * **Statistical Conclusion:** **Null Hypothesis $H_{1,0}$ is REJECTED ($p < 0.001$)**. Statistical significance confirmed.

#### **Hypothesis 2 (H2 - Customer Satisfaction Gain):**
* **Null Hypothesis ($H_{2,0}$):** T-AASA recommendations yield no higher user aspect satisfaction ($DV_2$) than baseline recommendations.
* **Alternative Hypothesis ($H_{2,1}$):** T-AASA recommendations significantly increase user aspect satisfaction for target aspect preferences.
* **Statistical Test Results:**
  * Baseline Top-1 Aspect Satisfaction: `0.1621`
  * T-AASA Top-1 Aspect Satisfaction: `0.2382`
  * **Relative Gain:** **+46.95% Satisfaction Increase**.
  * **Statistical Conclusion:** **Null Hypothesis $H_{2,0}$ is REJECTED**.

#### **Hypothesis 3 (H3 - Ground-Truth Verification Alignment):**
* **Null Hypothesis ($H_{3,0}$):** T-AASA recommendations show no higher alignment with ground-truth manual review text sentiment ($DV_3$) than baseline star ratings.
* **Alternative Hypothesis ($H_{3,1}$):** T-AASA recommendations achieve significantly higher alignment with ground-truth review inspection.
* **Statistical Test Results:**
  * SDMAE Ground-Truth Alignment: `20.0%`
  * T-AASA Ground-Truth Alignment: **`90.0%`** (**+70.0% Absolute Gain / +350.0% Relative Gain**).
  * **Statistical Conclusion:** **Null Hypothesis $H_{3,0}$ is REJECTED**.

---

## 🔐 SECTION 6: OPEN SCIENCE & REPRODUCIBILITY (Item 7)

All experimental code, raw CSV datasets, dataset line mappings, and statistical execution logs are formatted in compliance with **FAIR Science (Findable, Accessible, Interoperable, Reusable)** requirements:
* **Code Repository:** `experiment_code.py`
* **Dataset Mapping File:** `manual_review_dataset_mapping.csv`
* **Statistical Hypothesis Log:** `statistical_hypothesis_tests.txt`
