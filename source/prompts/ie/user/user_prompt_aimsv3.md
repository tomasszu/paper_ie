Extract information from the following excerpt from a study:

{chapter_json}

Use the following JSON response format to list the study aims IF there are any, oterwise return None.

{queried_fields_json}

Tips:

* An aim will most usually appear in the introduction after the gap in the literature and the main research question has already been adressed.
* The primary aims will usually come in the form of hypotheses where the authors are making a specific, testable claim.
* The primary aims we care about are not descriptive/observational, they will be inferential and directional in nature. The action verbs will most often be "hypothesize", "correlate", "predict".
* A secondary aim will most often be gated by a primary aim.
* An exploratory aim will be more open-ended, but must not precede a primary aim.

Rules:

* A single sentence can contain two or more aims. Such a sentence MUST be split by its action words.
* An aim that is a hypothesis MUST have action items.

