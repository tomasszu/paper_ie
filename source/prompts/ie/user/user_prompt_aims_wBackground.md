Extract information from the following chapter from a study:

{chapter_json}

Use the following JSON response format to list the study aims IF there are any, oterwise return None and the background available on the study.

{queried_fields_json}

Tips:

* A primary aim will most often read like a hypothesis.
* A secondary aim constitutes it having a parent aim.
* Exploratory aims are mostly open ended questions.
* Pay attention to the distinction between aims and the methods taken to achieve them. Do not include specific methodologies, like "we did x" or "y was done to ...".

