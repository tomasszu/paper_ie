- **Growth Mixture Model (GMM)**
  - COHORT: What are the distinct trajectory classes based on key sagittal spinopelvic parameters to understand different patient subgroups?

- **Shapiro-Wilk test**
  - COHORT: Is the distribution of continuous variables normal to determine the appropriate statistical methods for between-class comparisons?

- **ANOVA**
  - BETWEEN-CLASS: Are there significant differences in continuous variables with normal distribution across the four trajectory classes?

- **Kruskal-Wallis test**
  - BETWEEN-CLASS: Are there significant differences in continuous variables without normal distribution across the four trajectory classes?

- **Wilcoxon rank-sum test**
  - BETWEEN-CLASS: Are there significant differences in continuous variables between classes, particularly after normality checks?

- **Fisher exact test**
  - BETWEEN-CLASS: Are there significant differences in categorical variables between the classes?

- **Wilcoxon signed-rank test**
  - WITHIN-CLASS: Are there meaningful changes in sagittal alignment parameters within each trajectory class from preoperative to postoperative timepoints?

- **F-test (two-sample variance test)**
  - COHORT: Are there significant differences in the variances of key sagittal spinopelvic parameters across the full cohort?

- **Levene's test**
  - COHORT: Are there significant differences in the variances of key sagittal spinopelvic parameters across the full cohort?

- **Likelihood ratio test (LRT)**
  - COHORT: Are candidate predictors significant in a multinomial logistic model to refine the model for class prediction?

- **Spearman correlation matrix**
  - COHORT: What are the strength and direction of relationships between candidate predictors to inform model selection?

- **Pearson correlation**
  - COHORT: What is the strength and direction of relationships between PT, PI-LL, UIV_PA, L4PA, and a composite parameter to understand their interdependencies?

- **Bayesian Information Criterion (BIC)**
  - COHORT: Which statistical model is the best based on model fit and complexity?