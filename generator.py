import openai
import os
import json
from prompt_utils import render_prompt
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

CATEGORY_TO_PROMPT = {
    "electronics": "prompts/electronics_prompt.txt",
    "fashion": "prompts/fashion_prompt.txt",
    "skincare": "prompts/skincare_prompt.txt"
}

def generate_description(product_data, category):
    prompt_path = CATEGORY_TO_PROMPT.get(category)
    if not prompt_path:
        raise ValueError("Unsupported category")

    template = Path(prompt_path).read_text()
    prompt = render_prompt(template, product_data)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    product = json.load(open("data/sample_products.json"))['electronics'][0]
    desc = generate_description(product, "electronics")
    print(desc)
