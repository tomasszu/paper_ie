- **Growth Mixture Model (GMM)**
  - Population: Full cohort (N = 335 patients)
  - Variables: PT, UIV_PA, PI-LL, L4PA
  - Purpose: Primary analysis

- **Shapiro-Wilk test**
  - Population: Between classes
  - Variables: Continuous variables
  - Purpose: Preprocessing/validation step

- **ANOVA**
  - Population: Between classes
  - Variables: Continuous variables (normal distribution)
  - Purpose: Primary analysis

- **Kruskal-Wallis test**
  - Population: Between classes
  - Variables: Continuous variables (non-normal distribution)
  - Purpose: Primary analysis

- **Wilcoxon rank-sum test**
  - Population: Between classes
  - Variables: Continuous variables
  - Purpose: Primary analysis

- **Fisher exact test**
  - Population: Between classes
  - Variables: Categorical variables
  - Purpose: Primary analysis

- **Wilcoxon signed-rank test**
  - Population: Within each class
  - Variables: PT, UIV_PA, PI-LL, L4PA, SVA, T1PA, LL L1-S1, LL L4-S1, L1PA, T10-L2, TK T2-T12
  - Purpose: Primary analysis

- **F-test**
  - Population: Full cohort
  - Variables: PT, PI-LL, SVA, T1PA, UIV_PA, LL L1-S1
  - Purpose: Primary analysis

- **Levene's test**
  - Population: Full cohort
  - Variables: PT, PI-LL, SVA, T1PA, UIV_PA, LL L1-S1
  - Purpose: Primary analysis

- **Likelihood ratio test (LRT)**
  - Population: Full cohort
  - Variables: Candidate predictors in a multinomial logistic model
  - Purpose: Preprocessing/validation step

- **Spearman correlation matrix**
  - Population: Full cohort
  - Variables: Candidate predictors
  - Purpose: Preprocessing/validation step

- **Pearson correlation**
  - Population: Full cohort
  - Variables: PT, PI-LL, UIV_PA, L4PA, composite parameter (PI-LL + UIV_PA + L4PA)
  - Purpose: Primary analysis

- **Multinomial logistic regression**
  - Population: Full cohort
  - Variables: Baseline predictors, 6-week PI-LL
  - Purpose: Primary analysis

- **Bayesian Information Criterion (BIC)**
  - Population: Full cohort
  - Variables: Model selection
  - Purpose: Model selection/validation step

- **Normalized classification entropy**
  - Population: Full cohort
  - Variables: Model validation
  - Purpose: Model selection/validation step