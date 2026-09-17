Extract information from the following excerpt from a study:

{chapter_json}

Take into account these aims and background of the study:

{context_json}

Use the following JSON response format to list the study questions IF there are any, otherwise return None.

{queried_fields_json}

Tips:

* The questions need to be inferred from the methods used (like study design, model, cohort or parameter selection choices)
* The questions are NOT the same as the aims, as questions will usually be subdivisions of aims
* The individual questions should further the paper aims of finding something out
* If the aims and the background answered the "why" of the study, then the questions need to answer the "what" part, but not yet the "how", which is reserved for tests in the Results.
* Write each question at the level of the comparison or inferential goal, not at the level of a specific statistical test or parameter. 

Rules:

* Where multiple sub-questions share the same inferential unit (e.g. existence and enumeration of classes, or multiple model variants answering the same predictor question), collapse them into a single question.
* If between-group comparisons span both pre-operative and post-operative timepoints, split them into separate questions: one for baseline differences and one for postoperative differences across time.
* Treat non-radiographic baseline characteristics (demographics, comorbidities, surgical variables) as a distinct question from radiographic baseline differences.
* Exclude questions that reflect analyst-level mechanistic explorations unless they are explicitly tied to a stated aim.


