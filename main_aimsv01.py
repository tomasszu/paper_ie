import os
from pydantic import BaseModel
from pathlib import Path
import creds
import pprint
from typing import Optional

import langchain

import json
from typing import Any

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


# Set LangSmith environment variables BEFORE importing LangChain modules  
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = creds.LANGSMITH_ENDPOINT
os.environ["LANGSMITH_API_KEY"] = creds.LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = creds.LANGSMITH_PROJECT

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Lopading in the PDF file, parsing into markdown then to JSON and cleaning the JSON up >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#pdf_name = "The_Shape_of_the_Fused_Spine_is_Associated_With_Acute_Proximal_Junctional_Kyphosis_in_Adult_Spinal_Deformity_An_Assessment_Based_on_Vertebral_Pelvic_Angles"
#pdf_name = "pelvic_nonresponse_following_treatment_of_adult.7"
#pdf_name = "Lower_Limb_Khalife"
#pdf_name = "optimizing_the_definition_of_proximal_junctional.7"
#pdf_name = "posterior_ligamentous_augmentation_is_associated.9"
pdf_name = "Post_Discharge_Lorenzen"
#pdf_name = "PON_LT_GMM_Trajectories_FULL_DRAFT_MAY2026_v1"

input_chunks_dir = fr"C:\Users\lenox\OneDrive\Documents\tom\projects\pdf_parser\output\{pdf_name}\chunks"
# Output folder for answer json
output_folder = fr"C:\Users\lenox\tomass\projects\paper_ie\outputs\{pdf_name}"

# Helper function to read .md files  
def load_template(filepath):  
    with open(filepath, "r", encoding="utf-8") as file: 
        return file.read()

def render_simple(obj: dict) -> str:  
    lines = []  
    doc = obj["document"]  
    lines.append(doc["title"])  
    lines.append("")

    for section in doc.get("sections", []):  
        lines.append(section["heading"].upper())  
        lines.append("")

        for kid in section.get("kids", []):  
            # skip figures and tables  
            if kid.get("type") in ("figure", "table"):  
                continue

            content = kid.get("content", "")

            if kid.get("type") == "heading":  
                lines.append(content)  
            else:  
                lines.append(content)

            lines.append("")

    return "\n".join(lines).strip() + "\n"    


def main():

    model = init_chat_model(
        "qwen2.5:14b",
        model_provider="ollama",
        temperature=0.1,
        timeout=1200,
    )

    sys_prompt_ie = load_template(r"source\prompts\ie\system\sys_prompt.md")
    user_prompt_temp = load_template(r"source\prompts\ie\user\user_prompt_aims.md")

    try:
        with open(r"source\query_jsons\queried_aims.json", 'r') as f:
            qf_json = json.load(f)
            # Make JSON pretty (format it with indents)
            qf_json = json.dumps(qf_json, indent=2, ensure_ascii=False)
    except Exception as e:
        raise f"Fetch failed: {e}"

    input_path = Path(input_chunks_dir)
    output_path = Path(output_folder)

    output_path.mkdir(parents=True, exist_ok=True)

    for file_path in input_path.iterdir():
        if file_path.is_file() and "intro" in file_path.name:
            print(f"Loading: {file_path.name}")

            try:
                with open(file_path, 'r', encoding="utf-8") as f:
                    chunk = json.load(f)


            except Exception as e:
                raise f"Fetch failed: {e}"


            # Make JSON human readable
            chunk_text = render_simple(chunk)

            #print(chunk_text)
                
            user_prompt = user_prompt_temp.format(
                chapter_json = chunk_text, queried_fields_json = qf_json
            )

            print(user_prompt)

            ie_messages = [
                SystemMessage(content=sys_prompt_ie),
                HumanMessage(content=user_prompt)
            ]

            response = model.invoke(ie_messages)

            if response.content != "None":
                print(response.content)
                output_file_path = Path(  
                    output_path,  
                    f"{file_path.name}_aims.json"  
                )

                try:
                    with open(output_file_path, 'w', encoding="utf-8") as f:
                        f.write(response.content)

                except Exception as e:
                    raise f"Fetch failed: {e}"



if __name__ == '__main__': 
    main()
else:
    print("you imported this file from somewhere else")
