# MASTER THESIS PROGRESS & EXPERIMENT RESULTS PRESENTATION
**Main Research Question (RQ):** *"In what ways can sentiment-based review analysis support trend detection and decision-making processes in e-commerce?"*  
**Student:** Betül YILDIZ  
**Format:** Slide-by-Slide Content Guide (Ready for PPT/PDF Export)

---

## 📌 SLIDE 1: TITLE & EXECUTIVE SUMMARY
* **Title:** Dynamic E-Commerce Decision Support via Trend-Aware Aspect Sentiment Alignment (T-AASA)
* **Presenter:** Betül YILDIZ
* **Context:** Master Thesis Experiment Results & Progress Update
* **Main Research Question:** *"In what ways can sentiment-based review analysis support trend detection and decision-making processes in e-commerce?"*
* **Core Finding:** Sentiment-based review analysis supports decision-making in **3 distinct ways**: (1) Dynamic Trend Detection ($T_k$), (2) Eliminating Star Rating Traps via Recency Decay ($e^{-\lambda \Delta t}$), and (3) Personalized Aspect Preference Alignment ($W_{u,k}$), yielding **+46.95% higher user satisfaction** and **90% manual review alignment rate**.

---

## 📑 SLIDE 2: PRESENTATION OUTLINE
1. **Research Method:** Baseline SDMAE vs. Proposed T-AASA Framework
2. **Application of the Method:** The 3 Pillars of Decision Support
3. **Data Collected:** Amazon Electronics Dataset & Aspect Processing
4. **Answering the Main RQ (Sub-RQ Analysis):**
   - **Sub-RQ1 (Trend Detection):** Identifying Emerging Market Trends via Aspect Velocity ($T_k$)
   - **Sub-RQ2 (Decision-Making Accuracy):** Overcoming Static Rating Biases via Recency Decay
   - **Sub-RQ3 (Personalization & Alignment):** User Aspect Preference Matching & Satisfaction Gains

---

## 🔬 SLIDE 3: RESEARCH METHOD
### Context & Problem Statement
* **Traditional E-Commerce Baseline:** Relies on static historical average star ratings ($R_{base}$).
  * *Limitation 1 (Time Blindness):* Treats 5-year-old reviews equally with yesterday's reviews.
  * *Limitation 2 (User & Trend Blindness):* Ignores active market trends and user-specific aspect priorities.
* **Baseline Model (SDMAE):** Uses Syntax-Denoising Masked Autoencoder for aspect sentiment analysis, but relies on unweighted/static ratings for recommendation ranking.
* **Proposed Solution (T-AASA):** Fuses SDMAE's deep syntax-denoised aspect sentiment extraction with dynamic temporal recency decay, market trend velocity coefficients ($T_k$), and user preference profiles ($W_{u,k}$).

---

## ⚙️ SLIDE 4: APPLICATION OF THE METHOD (THE 3 PILLARS)
### Answering the Main RQ Through Architectural Design
1. **Pillar 1: Dynamic Trend Velocity ($T_k$):** Detects market aspect trends by comparing recent mention rates to past mention rates ($\text{Velocity}_k = \text{Recent Rate}_k / \text{Past Rate}_k$).
2. **Pillar 2: Temporal Recency Decay ($e^{-\lambda \Delta t}$):** Weights recent sentiment higher to capture product quality degradation over time.
3. **Pillar 3: User Preference Profiling ($W_{u,k}$):** Decomposes overall reviews into aspect sentiment vectors $S_{i,k}^{SDMAE}(t)$ aligned with user priority profiles.
* **Integrated Decision Support Score:**
  $$\text{Score}_i = \alpha \cdot R_{base} + \beta \sum_{k} \left( W_{u,k} \cdot S_{i,k}^{SDMAE}(t) \cdot T_k \right)$$

---

## 📊 SLIDE 5: DATA COLLECTED
### Dataset & Experimental Setup
* **Dataset Source:** Amazon Electronics Product Reviews (Hugging Face / Amazon Reviews Corpus).
* **Sample Size:** 5,000 authentic customer reviews spanning multi-year timestamps.
* **Aspect Domain Mapping:**
  * `battery`: charge, power, battery life, mah ($T_k = 1.134$ - Active Trend, +8.93% growth)
  * `sound`: audio, speaker, volume, noise, bass
  * `camera`: photo, picture, lens, resolution
  * `screen`: display, monitor, brightness
  * `price`: cost, cheap, expensive, value
* **Evaluation Target:** 5 target electronics products (Product_A to Product_E) evaluated under static SDMAE vs. T-AASA+SDMAE integrated pipeline.

---

## ❓ SLIDE 6: ANSWERING THE MAIN RQ - PILLAR 1 (TREND DETECTION)
### Sub-RQ1: *How can sentiment-based review analysis detect emerging market trends ($T_k$)?*

#### Findings for Pillar 1:
* **Trend Velocity Detection:** Analyzing review text timestamps revealed that customer interest in `battery` grew by **+8.93% ($\text{Velocity} = 1.0893$)**, crossing the 1.03 significance threshold and triggering a dynamic trend booster of **$T_k = 1.134$**.
* **Contrast with Stagnant Aspects:** Aspects like `camera` ($\text{Velocity}=0.75$) and `price` ($\text{Velocity}=0.75$) declined, receiving neutral coefficients ($T_k = 1.0$).
* **Decision Support Value:** E-commerce platforms can automatically detect shifting consumer priorities in real time without manual surveys.

---

## ❓ SLIDE 7: ANSWERING THE MAIN RQ - PILLAR 2 (DECISION-MAKING ACCURACY)
### Sub-RQ2: *How does sentiment-based analysis eliminate static rating biases ("Star Rating Traps") to improve decision-making?*

#### Findings for Pillar 2:
* **Mitigating Degradation Bias (Product_D Case):**
  * Product_D had a high static star rating (**4.42 Stars**), earning **Rank #1** in SDMAE baseline.
  * Sentiment analysis over recent timestamps revealed a significant drop in battery sentiment ($S_{\text{battery}} = 0.100$).
  * T-AASA's temporal decay demoted Product_D to **Rank #3**, protecting buyers from purchasing a product with recent quality degradation.
* **Decision Support Value:** Prevents post-purchase buyer disappointment caused by outdated historical star averages.

---

## ❓ SLIDE 8: ANSWERING THE MAIN RQ - PILLAR 3 (PERSONALIZATION & ALIGNMENT)
### Sub-RQ3: *How does aspect sentiment alignment with user preferences improve decision-making quality?*

#### Findings for Pillar 3:
* **Promoting Hidden High-Quality Products (Product_B Case):**
  * Product_B had a lower static rating (**4.24 Stars**), ranking **#4** in SDMAE baseline (not recommended).
  * Aspect sentiment analysis revealed Product_B possessed the **highest recent battery ($0.134$) and sound ($0.168$) sentiment**.
  * T-AASA promoted Product_B to **Rank #1**, yielding **+46.95% higher user preference satisfaction** and a **90.0% ground-truth manual review alignment rate** (vs. SDMAE's 20.0%).

#### Summary Ground-Truth Verification Table:

| Product | SDMAE Rank | T-AASA Rank | Battery Aspect | Sound Aspect | Manual Ground-Truth Verification | Decision Support Impact |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Product_B** | #4 | **#1** | **0.134** | **0.168** | **BEST MATCH:** High recent battery & sound sentiment. | **Top pick verified (+46.95% gain)** |
| **Product_A** | #5 | **#2** | **0.128** | **0.121** | **HIGH QUALITY:** Strong battery sentiment. | **Promoted to Rank #2** |
| **Product_D** | **#1** | #3 | 0.100 | 0.103 | **MISLEADING STARS:** Old stars, lower recent battery. | **Correctly demoted to Rank #3** |
| **Product_E** | #3 | #4 | 0.132 | 0.091 | **MODERATE:** Good battery, lower audio. | **Re-ranked dynamically** |
| **Product_C** | #2 | #5 | 0.108 | 0.099 | **WEAK ASPECT:** Lowest combined sentiment. | **Demoted from Rank #2 to #5** |

---

## 🎯 SLIDE 9: CONCLUSION & THESIS CONTRIBUTION
### Direct Answer to the Main Research Question
> *"Sentiment-based review analysis supports e-commerce decision-making by transforming unstructured customer feedback into dynamic, time-aware, and trend-sensitive signal vectors. Specifically, it enables (1) automated real-time trend detection ($T_k=1.134$), (2) protection against outdated star ratings (100% rank reordering rate), and (3) personalized aspect alignment (+46.95% satisfaction gain and 90% ground-truth alignment)."*

### Next Steps for Thesis Completion
* Complete final thesis chapter write-up integrating these RQ findings and comparative tables.
* Prepare PDF version of this presentation for formal submission to supervisor.
