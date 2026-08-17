# MASTER THESIS STRUCTURE & DETAILED OUTLINE
**Thesis Title:** Dynamic Customer Satisfaction Modeling via Trend-Aware Aspect Sentiment Alignment (T-AASA) Integrated with SDMAE Baseline  
**Student:** Betül YILDIZ  
**Advisor:** Prof. Camille Salinesi (Université Paris 1 Panthéon - Sorbonne)  
**Target Page Count:** ~75 - 85 Pages (~22,000 - 25,000 Words)

---

## 📐 SECTION-BY-SECTION THESIS OUTLINE & PAGE ESTIMATES

```
====================================================================================================
CHAPTER / SECTION TITLE                                           ESTIMATED PAGES    ESTIMATED WORDS
====================================================================================================
PREAMBLE & FRONT MATTER (Abstract, Acknowledgments, Contents)           4 Pages          ~1,000 Words
CHAPTER 1: INTRODUCTION & PROBLEM STATEMENT                            10 Pages          ~3,000 Words
  1.1 Context & Motivation in E-Commerce
  1.2 The Limitation of Static Average Star Ratings (Illustrative Ex.)
  1.3 Primary Research Question (Main RQ) & Sub-RQs
  1.4 Scope & Terminology Clarifications (Sentiment vs. Satisfaction vs. Recommendation)
  1.5 Thesis Structure & Contributions
CHAPTER 2: LITERATURE REVIEW & RELATED WORKS                           14 Pages          ~4,200 Words
  2.1 Aspect-Based Sentiment Analysis (ABSA) & SDMAE Model
  2.2 Limitations of Traditional Collaborative & Content Filtering
  2.3 Temporal Recency Decay & Feature Drift in E-Commerce
  2.4 Market Trend Velocity Modeling in Customer Review Mining
CHAPTER 3: THE PROPOSED METHOD (REUSABLE SCIENTIFIC RECIPE)             12 Pages          ~3,500 Words
  3.1 Mathematical Formulation of T-AASA Framework
  3.2 Module A: Temporal Recency Decay Modeling (exp(-lambda * dt))
  3.3 Module B: Market Trend Velocity Coefficient (Tk)
  3.4 Module C: User Aspect Preference Profiling (W_{u,k})
  3.5 Module D: Fusion Engine & Integrated Scoring Formula
CHAPTER 4: APPLICATION OF THE METHOD & EXPERIMENTAL PROTOCOL           12 Pages          ~3,500 Words
  4.1 Dataset Characteristics & Frequencies (Amazon Electronics)
  4.2 Aspect Mapping & Domain Keyword Dictionaries
  4.3 Experimental Setup: Baseline SDMAE vs. T-AASA Integration
  4.4 Reproducibility Protocol & Open Science (FAIR Principles)
CHAPTER 5: EMPIRICAL RESULTS & HYPOTHESIS TESTING (RQ BY RQ)          16 Pages          ~4,800 Words
  5.1 Structural Equation Model (SEM) & Variables (IVs vs. DVs)
  5.2 Formal Hypotheses Formulation (Null H0 vs. Alternative H1-H3)
  5.3 RQ1 Analysis: Rank Divergence & Score Shift (p < 0.001)
  5.4 RQ2 Analysis: Customer Satisfaction Score Gains (+46.95%)
  5.5 RQ3 Analysis: Ground-Truth Manual Review Verification (90% vs 20%)
  5.6 Discussion & Threats to Validity
CHAPTER 6: CONCLUSION, REFLECTIONS & FUTURE WORK                       5 Pages          ~1,500 Words
  6.1 Summary of Findings & Scientific Contributions
  6.2 Personal Experience & Lessons Learned
  6.3 Future Research Directions & Open Science Repository
APPENDICES (Code, Complete Data Tables, Statistical Logs)              10 Pages          ~2,000 Words
====================================================================================================
TOTAL ESTIMATED THESIS SIZE                                            83 Pages         ~24,500 Words
====================================================================================================
```

---

## 📌 CHAPTER-BY-CHAPTER DETAILED CONTENT DESCRIPTION

### 📖 CHAPTER 1: INTRODUCTION & PROBLEM STATEMENT (10 Pages)
* **1.1 Motivation:** E-commerce decision-making relies heavily on online customer feedback.
* **1.2 Illustrative Example (Discrepancy Problem):** Concrete scenario showing Product_D with a legacy star rating of **4.42 stars** from 2018. However, recent reviews in 2021 reveal battery degradation ($S=0.100$). Traditional star averages create a severe discrepancy between *computed satisfaction* and *actual current customer satisfaction*.
* **1.3 Terminology Clarification (Scope Boundary):**
  * *Sentiment Analysis:* Extracting numerical polarity scores from raw text (Out of scope of innovation; performed via SDMAE).
  * *Customer Satisfaction Metric:* Combining sentiment, recency decay, and trend velocity into a dynamic satisfaction score (Primary scope of innovation: T-AASA).
  * *Recommendation:* Downstream application using collaborative/content filtering (Out of scope; used as benchmark context).

### 📖 CHAPTER 2: LITERATURE REVIEW & PRIOR WORKS (14 Pages)
* Quoting prior seminal works on rating bias (Resnick et al., Hu et al.), temporal feature decay (Gama et al., Koren), and aspect sentiment analysis (Tai et al. - SDMAE).

### 📖 CHAPTER 3: THE PROPOSED METHOD (REUSABLE SCIENTIFIC RECIPE) (12 Pages)
* Generic, domain-independent scientific specification of T-AASA. Another researcher can apply Chapter 3 to hotel reviews, app reviews, or restaurant datasets.

### 📖 CHAPTER 4: APPLICATION OF THE METHOD (12 Pages)
* Specific instantiation on **Amazon Electronics dataset** (5,000 reviews, products Product_A to Product_E, aspect frequency distribution tables).

### 📖 CHAPTER 5: EMPIRICAL RESULTS & HYPOTHESIS TESTING (16 Pages)
* **Structural Model & Variables:**
  * *Independent Variables (IVs):* Model Type (Static vs Dynamic), Timestamp Difference ($\Delta t$), Aspect Trend Velocity ($T_k$), User Aspect Weights ($W_{u,k}$).
  * *Dependent Variables (DVs):* Recommendation Rank, Customer Satisfaction Score, Ground-Truth Alignment Rate.
* **Hypotheses & Statistical Tests:**
  * $H_1$: T-AASA dynamic scores deviate significantly from static baseline scores ($t = 10.22, p < 0.001$, Wilcoxon $W = 4952.5, p < 0.001$). Null $H_{1,0}$ REJECTED.
  * $H_2$: T-AASA yields statistically superior user aspect satisfaction (+46.95% gain). Null $H_{2,0}$ REJECTED.
  * $H_3$: T-AASA achieves higher ground-truth manual review alignment (90.0% vs 20.0%). Null $H_{3,0}$ REJECTED.

### 📖 CHAPTER 6: CONCLUSION & FUTURE WORK (5 Pages)
* Summary of contributions, personal reflections on the thesis project, and roadmap for journal publication.
