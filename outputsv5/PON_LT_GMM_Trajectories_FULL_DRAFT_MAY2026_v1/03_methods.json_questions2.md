- **Growth Mixture Model (GMM)**
  - COHORT: Identify distinct trajectory classes based on key sagittal spinopelvic parameters to understand different patient subgroups.

- **Shapiro-Wilk test**
  - COHORT: Assess the normality of continuous variables to determine the appropriate statistical methods for between-class comparisons.

- **ANOVA**
  - BETWEEN-CLASS: Determine if there are significant differences in continuous variables with normal distribution across the four trajectory classes.

- **Kruskal-Wallis test**
  - BETWEEN-CLASS: Determine if there are significant differences in continuous variables without normal distribution across the four trajectory classes.

- **Wilcoxon rank-sum test**
  - BETWEEN-CLASS: Determine if there are significant differences in continuous variables between classes, particularly after normality checks.

- **Fisher exact test**
  - BETWEEN-CLASS: Determine if there are significant differences in categorical variables between the classes.

- **Wilcoxon signed-rank test**
  - WITHIN-CLASS: Assess if there are meaningful changes in sagittal alignment parameters within each trajectory class from preoperative to postoperative timepoints.

- **F-test (two-sample variance test)**
  - COHORT: Determine if there are significant differences in the variances of key sagittal spinopelvic parameters across the full cohort.

- **Levene's test**
  - COHORT: Determine if there are significant differences in the variances of key sagittal spinopelvic parameters across the full cohort.

- **Likelihood ratio test (LRT)**
  - COHORT: Determine the significance of candidate predictors in a multinomial logistic model to refine the model for class prediction.

- **Spearman correlation matrix**
  - COHORT: Assess the strength and direction of relationships between candidate predictors to inform model selection.

- **Pearson correlation**
  - COHORT: Determine the strength and direction of relationships between PT, PI-LL, UIV_PA, L4PA, and a composite parameter to understand their interdependencies.

- **Bayesian Information Criterion (BIC)**
  - COHORT: Compare and select the best statistical model based on model fit and complexity.