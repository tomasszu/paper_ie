You are completing Step 2 of a multi-step extraction task.

You have been given:  
1. A structured description of the study population, groupings,   
   and parameters (DESCRIPTION)  
2. A structured inventory of every statistical test and model   
   used, including what population and variables each was   
   applied to (TEST INVENTORY)

Your task: for each entry in the TEST INVENTORY, write one   
sentence stating what is being found out.

Rules:  
- For each test, write what question it is trying to answer   
  from the researcher's perspective — what do they want to know?  
- You may name the analysis type broadly (e.g. "correlation",   
  "class comparison") but do not describe the test mechanism  
- Include the clinical or scientific meaning where apparent —   
  why does this comparison matter for understanding the data?  
- Preprocessing steps (normality checks, collinearity checks)   
  should be noted as serving the primary analysis they enable,   
  not skipped entirely  
- Assign each entry to one level:   
  COHORT / BETWEEN-CLASS / WITHIN-CLASS  
- Keep one entry per test — do not collapse yet

EXAMPLE:

Input entry:  
- Wilcoxon signed-rank test  
  - Population: Within each class  
  - Variables: PT, PI-LL, UIV_PA, L4PA, SVA, T1PA...

What NOT to write:  
"To assess changes in radiographic parameters within each   
class over time" ❌

What TO write:  
"WITHIN-CLASS: Within each trajectory class, does surgery   
produce meaningful changes in sagittal alignment from   
preoperative to 6 weeks and 2 years, and do the magnitude   
and pattern of those changes differ across classes?" ✅

The difference: name the timepoints, frame it as a clinical   
question, note what would make the finding meaningful.

DESCRIPTION:  
{step_1a_json}

TEST INVENTORY:  
{step_1b_json}

NOTE:
Do not ask any follow up questions in this output to the user!!!