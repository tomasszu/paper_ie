**1 – Multivariate Growth Mixture Model (GMM) – 4‑class solution**  
COHORT: The full cohort of patients with complete pre‑operative, 6‑week, and 2‑year data is used to identify four distinct longitudinal trajectories of pelvic tilt (PT), PI‑LL mismatch, UIV pelvic angle (UIV_PA), and L4 pelvic angle (L4PA) over time.

**2 – Fixed effects: quadratic time trend in GMM**  
COHORT: The model incorporates both linear and quadratic components of the time variable to capture potential non‑linear changes in the four radiographic outcomes across the three follow‑up points.

**3 – Random slope for time in GMM**  
COHORT: A random effect on the time slope allows individual patients to deviate from the average trajectory, reflecting patient‑specific variation in how their sagittal parameters evolve post‑operatively.

**4 – Grid search for class number (1–5) with random starts and iterations**  
COHORT: Multiple model fits are run across 1–5 latent classes using many random initializations to ensure robust exploration of the optimal number of trajectory groups.

**5 – Bayesian Information Criterion (BIC) to choose optimal class number**  
COHORT: BIC values from each candidate model guide selection of the most parsimonious class solution that balances fit and complexity.

**6 – Minimum class size criterion (n ≥ 20)**  
COHORT: Only models yielding at least 20 patients per latent class are considered acceptable, ensuring statistical stability within each trajectory group.

**7 – Normalized classification entropy calculation**  
COHORT: Entropy of posterior class probabilities is computed to assess the clarity of class assignment; higher entropy indicates more distinct grouping.

**8 – Posterior probability thresholds (>0.70, >0.80, >0.90)**  
COHORT: Patients with posterior membership probabilities above these cut‑offs are flagged as having confident class assignments for downstream analyses.

**9 – Shapiro–Wilk test for normality (continuous variables) in between‑class comparisons**  
BETWEEN-CLASS: Continuous radiographic and outcome measures at the 1‑year timepoint are tested for normality to determine appropriate parametric or non‑parametric group comparison methods.

**10 – ANOVA (for normally distributed continuous variables) in between‑class comparisons**  
BETWEEN-CLASS: When normality holds, an analysis of variance evaluates whether mean values of a given variable differ across the four trajectory classes at 1 year.

**11 – Kruskal–Wallis test (for non‑normally distributed continuous variables) in between‑class comparisons**  
BETWEEN-CLASS: For skewed data, this rank‑based test assesses differences among class means at 1 year.

**12 – Eta‑squared (η²) effect size for ANOVA**  
BETWEEN-CLASS: The proportion of variance explained by class membership is quantified to gauge the practical importance of any significant ANOVA findings.

**13 – Epsilon‑squared (ε²) effect size for Kruskal–Wallis**  
BETWEEN-CLASS: An analogous non‑parametric effect size estimates how strongly class grouping influences a variable when data are not normally distributed.

**14 – Wilcoxon rank‑sum test (unadjusted and Bonferroni‑corrected) for pairwise post‑hoc comparisons in between‑class analyses**  
BETWEEN-CLASS: After an overall group difference is detected, this non‑parametric test compares each pair of classes while controlling the family‑wise error rate.

**15 – Compact Letter Display (CLD) algorithm for 4 classes**  
BETWEEN-CLASS: The CLD translates significant pairwise comparisons into a concise lettering scheme that visually indicates which classes differ from one another.

**16 – Fisher exact test (simulated p‑value, B = 5000 replicates) for categorical variables in between‑class comparisons**  
BETWEEN-CLASS: Categorical outcomes at 1 year are compared across trajectory groups using an exact test with Monte‑Carlo simulation to obtain accurate p‑values.

**17 – Wilcoxon signed‑rank test (paired) within each class**  
WITHIN-CLASS: For every latent class, this test evaluates whether each radiographic parameter (PT, UIV_PA, PI‑LL, L4PA, SVA, T1PA, LL L1‑S1, LL L4‑S1, L1PA, T10‑L2, TK T2‑T12) changes significantly from pre‑operative to 6 weeks and from pre‑operative to 2 years.

**18 – Standard Deviation (SD) ratio calculation (SD at 2Y / SD at pre‑op)**  
VARIANCE CONVERGENCE: The ratio of standard deviations at 2 years versus baseline quantifies whether variability in a parameter has narrowed or widened over time across the cohort.

**19 – Two‑sample F‑test for variance change from pre‑op to 2 yr**  
VARIANCE CONVERGENCE: This test formally assesses whether the overall variance of each selected variable differs significantly between the two timepoints.

**20 – Levene’s test for equality of variance across the 4 classes at pre‑op and 2 yr**  
VARIANCE CONVERGENCE: Levene’s test checks if variability in a parameter is homogeneous among trajectory groups, validating assumptions for subsequent analyses.

**21 – Likelihood Ratio Test (LRT) in multinomial logistic regression for univariable predictor screening**  
PREDICTOR ANALYSIS: Each candidate baseline or early postoperative predictor is compared to a null model; significant LRTs identify variables worthy of multivariable modeling.

**22 – Spearman correlation matrix for collinearity assessment among predictors**  
PREDICTOR ANALYSIS: Pairwise Spearman correlations are examined; highly correlated pairs (|r| > 0.60) are excluded to avoid multicollinearity in the multinomial logistic models.

**23 – Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model A (baseline predictors only)**  
PREDICTOR ANALYSIS: Baseline variables that best explain class membership, as judged by Akaike Information Criterion, are retained to form a parsimonious predictive model with Class 2 as the reference.

**24 – Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model B (baseline + 6‑week PI‑LL)**  
PREDICTOR ANALYSIS: The same stepwise procedure is repeated after adding the early postoperative PI‑LL value to determine whether it improves prediction of trajectory class.

**25 – Pearson correlation between 2‑year PT and each of three geometric parameters (PI‑LL, UIV_PA, L4PA) at matched timepoints**  
CONSTRUCT GEOMETRY–PELVIC ORIENTATION: This exploratory analysis investigates how the sagittal balance measured by PT relates to individual pelvic or spinal alignment components at both 6 weeks and 2 years.

**26 – Pearson correlation between 2‑year PT and simple additive composite (PI‑LL + UIV_PA + L4PA)**  
CONSTRUCT GEOMETRY–PELVIC ORIENTATION: A combined metric of pelvic and spinal alignment is correlated with PT to assess whether a unified construct better explains sagittal balance.

**27 – Within‑class Pearson correlation between L4PA and PT for Class 3 at 6 wk and 2 yr**  
CONSTRUCT GEOMETRY–PELVIC ORIENTATION (Class 3): For the large‑correction phenotype, this analysis tests whether changes in L4 pelvic angle are tightly linked to changes in PT over time.