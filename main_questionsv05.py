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
#pdf_name = "Post_Discharge_Lorenzen"
pdf_name = "PON_LT_GMM_Trajectories_FULL_DRAFT_MAY2026_v1"

input_chunks_dir = fr"C:\Users\lenox\OneDrive\Documents\tom\projects\pdf_parser\output\{pdf_name}\chapters"
# Output folder for answer json
output_folder = fr"C:\Users\lenox\tomass\projects\paper_ie\outputsv5\{pdf_name}"

# Helper function to read .md files  
def load_template(filepath):  
    with open(filepath, "r", encoding="utf-8") as file: 
        return file.read()

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            file = json.load(f)
            # Make JSON pretty (format it with indents)
            jfile = json.dumps(file, indent=2, ensure_ascii=False)
            return jfile
    except Exception as e:
        raise Exception(f"Fetch failed: {e}")

def write_file(output_path, file_path, file, name_appendix):
    output_file_path = Path(  
        output_path,  
        f"{file_path.name}_{name_appendix}"
    )

    try:
        with open(output_file_path, 'w', encoding="utf-8") as f:
            f.write(file)

    except Exception as e:
        raise f"Fetch failed: {e}"

def forward_pass(sys_prmt, usr_prmt, model):
    ie_messages = [
        SystemMessage(content=sys_prmt),
        HumanMessage(content=usr_prmt)
    ]

    response = model.invoke(ie_messages)

    return response

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
        temperature=0.5,
        timeout=1200,
    )

    sys_prompt_ie = load_template(r"source\prompts\ie\system\sys_prompt.md")

    # qf_json = load_json(r"source\query_jsons\queried_questions.json")
    # context_json = load_json(fr"outputsv2\{pdf_name}\02_introduction.json_aims.json")

    input_path = Path(input_chunks_dir)
    output_path = Path(output_folder)

    output_path.mkdir(parents=True, exist_ok=True)

    for file_path in input_path.iterdir():
        if file_path.is_file() and "methods" in file_path.name:
            print(f"Loading: {file_path.name}")

            try:
                with open(file_path, 'r', encoding="utf-8") as f:
                    chunk = json.load(f)


            except Exception as e:
                raise f"Fetch failed: {e}"


            # Make JSON human readable
            chunk_text = render_simple(chunk)

            """
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Step 1: List every distinct analytic block in the methods>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
              
            """
            user_prompt_temp = load_template(r"source\prompts\ie\user\question_steps\stepv5_1.md")
                
            user_prompt = user_prompt_temp.format(
                chapter_json = chunk_text
            )

            print(user_prompt)

            response = forward_pass(sys_prompt_ie, user_prompt, model)

            step1_content = response.content

            if step1_content != "None":
                print(step1_content)
                write_file(output_path, file_path, step1_content, name_appendix="questions1.md")

            """
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Step 2: inferential goal for each analytic block>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
              
            """
            user_prompt_temp = load_template(r"source\prompts\ie\user\question_steps\stepv5_2.md")

            user_prompt = user_prompt_temp.format(
                chapter_json = chunk_text, step_1_json = step1_content
            )

            print(user_prompt)

            response = forward_pass(sys_prompt_ie, user_prompt, model)

            step2_content = response.content

            if step2_content != "None":
                print(step2_content)
                write_file(output_path, file_path, step2_content, name_appendix="questions2.md")





if __name__ == '__main__': 
    main()
else:
    print("you imported this file from somewhere else")
