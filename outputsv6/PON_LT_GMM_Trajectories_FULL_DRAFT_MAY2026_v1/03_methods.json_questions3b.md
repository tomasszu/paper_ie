**Final List of Research Questions with Level Assignments**

1 – Multivariate Growth Mixture Model (GMM) – 4‑class solution  
*COHORT:* What distinct longitudinal trajectories of pelvic tilt (PT), PI‑LL mismatch, UIV pelvic angle (UIV_PA), and L4 pelvic angle (L4PA) can be identified across pre‑operative, 6‑week, and 2‑year follow‑up in the full cohort of patients with complete data?  

2 – Fixed effects: quadratic time trend in GMM  
*COHORT:* How do linear and quadratic components of time influence the evolution of PT, PI‑LL mismatch, UIV_PA, and L4PA across pre‑operative, 6‑week, and 2‑year assessments in the cohort?  

3 – Random slope for time in GMM  
*COHORT:* To what extent does individual patient variation in the rate of change over time affect PT, PI‑LL mismatch, UIV_PA, and L4PA trajectories post‑operatively within the cohort?  

4 – Grid search for class number (1–5) with random starts and iterations  
*COHORT:* Which latent class solution (between 1 and 5 classes) best captures distinct sagittal parameter trajectories when multiple random initializations are employed in the cohort?  

5 – Bayesian Information Criterion (BIC) to choose optimal class number  
*COHORT:* Based on BIC values, which latent class model provides the most parsimonious fit for PT, PI‑LL mismatch, UIV_PA, and L4PA trajectories across timepoints in the cohort?  

6 – Minimum class size criterion (n ≥ 20)  
*COHORT:* Which latent class solutions yield at least 20 patients per class, ensuring statistical stability of trajectory groups within the cohort?  

7 – Normalized classification entropy calculation  
*COHORT:* How clear is the assignment of patients to each latent class when evaluating normalized classification entropy for PT, PI‑LL mismatch, UIV_PA, and L4PA trajectories in the cohort?  

8 – Posterior probability thresholds (>0.70, >0.80, >0.90)  
*COHORT:* Which patients achieve posterior membership probabilities above 0.70, 0.80, or 0.90 for each latent class of PT, PI‑LL mismatch, UIV_PA, and L4PA trajectories in the cohort?  

9 – Shapiro–Wilk test for normality (continuous variables) in between‑class comparisons  
*BETWEEN-CLASS:* Are continuous radiographic and outcome measures at 1 year normally distributed across the four trajectory classes in the cohort?  

10 – ANOVA (for normally distributed continuous variables) in between‑class comparisons  
*BETWEEN-CLASS:* Do mean values of a given normally distributed variable differ among the four trajectory classes at 1 year in the cohort?  

11 – Kruskal–Wallis test (for non‑normally distributed continuous variables) in between‑class comparisons  
*BETWEEN-CLASS:* Are there differences in median values of a skewed variable across the four trajectory classes at 1 year in the cohort?  

12 – Eta‑squared (η²) effect size for ANOVA  
*BETWEEN-CLASS:* What proportion of variance in a normally distributed variable is explained by class membership at 1 year among cohort participants?  

13 – Epsilon‑squared (ε²) effect size for Kruskal–Wallis  
*BETWEEN-CLASS:* How strongly does class grouping influence a non‑normally distributed variable at 1 year in the cohort?  

14 – Wilcoxon rank‑sum test (unadjusted and Bonferroni‑corrected) for pairwise post‑hoc comparisons in between‑class analyses  
*BETWEEN-CLASS:* Which specific pairs of trajectory classes differ significantly on a non‑normally distributed variable at 1 year after adjusting for multiple comparisons in the cohort?  

15 – Compact Letter Display (CLD) algorithm for 4 classes  
*BETWEEN-CLASS:* How can significant pairwise differences among the four trajectory classes be succinctly represented using letters for each variable at 1 year in the cohort?  

16 – Fisher exact test (simulated p‑value, B = 5000 replicates) for categorical variables in between‑class comparisons  
*BETWEEN-CLASS:* Are categorical outcomes at 1 year distributed differently across the four trajectory classes in the cohort when using a Monte‑Carlo simulated Fisher exact test?  

17 – Wilcoxon signed‑rank test (paired) within each class  
*WITHIN-CLASS:* Does each radiographic parameter (PT, UIV_PA, PI‑LL mismatch, L4PA, SVA, T1PA, LL L1‑S1, LL L4‑S1, L1PA, T10‑L2, TK T2‑T12) change significantly from pre‑operative to 6 weeks and from pre‑operative to 2 years within each latent class in the cohort?  

18 – Standard Deviation (SD) ratio calculation (SD at 2Y / SD at pre‑op)  
*VARIANCE CONVERGENCE:* How does the variability of a parameter change from baseline to 2 years across the entire cohort, as indicated by the ratio of standard deviations?  

19 – Two‑sample F‑test for variance change from pre‑op to 2 yr  
*VARIANCE CONVERGENCE:* Is there a statistically significant difference in overall variance of each selected variable between pre‑operative and 2‑year timepoints across the cohort?  

20 – Levene’s test for equality of variance across the 4 classes at pre‑op and 2 yr  
*VARIANCE CONVERGENCE:* Are variances of a parameter homogeneous among the four trajectory classes at pre‑operative and at 2 years in the cohort?  

21 – Likelihood Ratio Test (LRT) in multinomial logistic regression for univariable predictor screening  
*PREDICTOR ANALYSIS:* Which baseline or early postoperative predictors show a significant improvement over a null model when predicting trajectory class membership in the cohort?  

22 – Spearman correlation matrix for collinearity assessment among predictors  
*PREDICTOR ANALYSIS:* Which pairs of candidate predictors exhibit high Spearman correlations (|r| > 0.60) that would warrant exclusion to avoid multicollinearity in multinomial logistic models within the cohort?  

23 – Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model A (baseline predictors only)  
*PREDICTOR ANALYSIS:* Which baseline variables are retained after bidirectional stepwise AIC selection to best predict class membership, using Class 2 as reference, in the cohort?  

24 – Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model B (baseline + 6‑week PI‑LL)  
*PREDICTOR ANALYSIS:* Does adding early postoperative PI‑LL to baseline predictors improve class membership prediction after bidirectional stepwise AIC selection in the cohort?  

25 – Pearson correlation between 2‑year PT and each of three geometric parameters (PI‑LL, UIV_PA, L4PA) at matched timepoints  
*CONSTRUCT GEOMETRY–PELVIC ORIENTATION:* How strongly is 2‑year pelvic tilt correlated with PI‑LL mismatch, UIV_PA, and L4PA measured at both 6 weeks and 2 years in the cohort?  

26 – Pearson correlation between 2‑year PT and simple additive composite (PI‑LL + UIV_PA + L4PA)  
*CONSTRUCT GEOMETRY–PELVIC ORIENTATION:* What is the relationship between 2‑year pelvic tilt and the combined metric of PI‑LL, UIV_PA, and L4PA in the cohort?  

27 – Within‑class Pearson correlation between L4PA and PT for Class 3 at 6 wk and 2 yr  
*CONSTRUCT GEOMETRY–PELVIC ORIENTATION (Class 3):* In patients classified as Class 3, how tightly are changes in L4 pelvic angle linked to changes in pelvic tilt at 6 weeks and at 2 years?