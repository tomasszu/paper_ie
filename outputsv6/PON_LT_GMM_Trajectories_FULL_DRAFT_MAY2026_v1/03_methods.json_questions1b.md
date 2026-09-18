**Statistical tests / models / analytical procedures mentioned in the Methods text**

| # | Procedure | Population applied to | Variables involved | Primary analysis or preprocessing/validation |
|---|-----------|-----------------------|--------------------|---------------------------------------------|
| 1 | Multivariate Growth Mixture Model (GMM) – 4‑class solution | Full cohort (complete‑case patients with data at all three timepoints, N = 335) | PT, PI‑LL, UIV_PA, L4PA (all four outcomes simultaneously) | Primary analysis |
| 2 | Fixed effects: quadratic time trend (linear + quadratic) in GMM | Full cohort | Time variable (pre‑op, 6 wk, 2 yr) | Model specification |
| 3 | Random slope for time in GMM | Full cohort | Time variable | Model specification |
| 4 | Grid search for class number (1–5 classes) with random starts and iterations | Full cohort | – | Model selection |
| 5 | Bayesian Information Criterion (BIC) to choose optimal class number | Full cohort | – | Model selection |
| 6 | Minimum class size criterion (n ≥ 20) | Full cohort | – | Model selection |
| 7 | Normalized classification entropy calculation | Full cohort | Posterior probabilities of class membership | Validation / quality metric |
| 8 | Posterior probability thresholds (>0.70, >0.80, >0.90) | Full cohort | Posterior probabilities | Validation / quality metric |
| 9 | Shapiro‑Wilk test for normality (continuous variables) | Between‑class comparisons (all classes) | Continuous variables at one‑year timepoint | Preprocessing check |
|10 | ANOVA (for normally distributed continuous variables) | Between‑class comparisons | Continuous variables at one‑year timepoint | Primary analysis |
|11 | Kruskal‑Wallis test (for non‑normally distributed continuous variables) | Between‑class comparisons | Continuous variables at one‑year timepoint | Primary analysis |
|12 | Eta‑squared (η²) effect size for ANOVA | Between‑class comparisons | ANOVA results | Effect size calculation |
|13 | Epsilon‑squared (ε²) effect size for Kruskal‑Wallis | Between‑class comparisons | Kruskal‑Wallis results | Effect size calculation |
|14 | Wilcoxon rank‑sum test (unadjusted and Bonferroni‑corrected) for pairwise post‑hoc comparisons | Between‑class comparisons | Continuous variables at one‑year timepoint | Post‑hoc analysis |
|15 | Compact Letter Display (CLD) algorithm for 4 classes | Between‑class comparisons | Pairwise p‑values from Wilcoxon rank‑sum | Post‑hoc visualization |
|16 | Fisher exact test (simulated p‑value, B = 5000 replicates) for categorical variables | Between‑class comparisons | Categorical variables at one‑year timepoint | Primary analysis |
|17 | Wilcoxon signed‑rank test (paired) within each class | Within‑class paired comparisons | GMM parameters and additional radiographic measures (SVA, T1PA, LL L1‑S1, LL L4‑S1, L1PA, T10‑L2, TK T2‑T12) pre‑op vs 6 wk; pre‑op vs 2 yr | Primary analysis |
|18 | Standard Deviation (SD) ratio calculation (SD at 2Y / SD at pre‑op) | Variance convergence (funneling effect) | SDs of selected variables | Descriptive statistic |
|19 | Two‑sample F‑test for variance change from pre‑op to 2 yr | Cohort overall | SDs of selected variables | Primary analysis |
|20 | Levene’s test for equality of variance across the 4 classes at pre‑op and 2 yr | Variance convergence | SDs of selected variables per class | Validation / homogeneity check |
|21 | Likelihood Ratio Test (LRT) in multinomial logistic regression for univariable predictor screening | Predictor analysis | Each candidate predictor vs null model | Preprocessing / variable selection |
|22 | Spearman correlation matrix for collinearity assessment | Predictor analysis | Pairwise correlations among predictors | Preprocessing / variable selection |
|23 | Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model A (baseline predictors only) | Predictor analysis | Baseline predictors | Primary analysis |
|24 | Stepwise AIC selection (bidirectional) in multinomial logistic regression – Model B (baseline + 6‑week PI‑LL) | Predictor analysis | Baseline predictors + 6‑wk PI‑LL | Primary analysis |
|25 | Pearson correlation between 2‑year PT and each of three geometric parameters (PI‑LL, UIV_PA, L4PA) at matched timepoints | Construct geometry–pelvic orientation analysis | PT, PI‑LL, UIV_PA, L4PA | Exploratory analysis |
|26 | Pearson correlation between 2‑year PT and simple additive composite (PI‑LL + UIV_PA + L4PA) | Construct geometry–pelvic orientation analysis | PT, composite variable | Exploratory analysis |
|27 | Within‑class Pearson correlation between L4PA and PT for Class 3 at 6 wk and 2 yr | Construct geometry–pelvic orientation analysis (Class 3 only) | L4PA, PT | Exploratory analysis |

*All procedures are listed exactly as they appear in the Methods text. No additional calculations or assumptions have been made.*