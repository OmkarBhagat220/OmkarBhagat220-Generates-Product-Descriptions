# 🛍️ Product Description Generator

This system generates category-specific product descriptions for e-commerce platforms using LLMs.

## 🧩 Features
- Prompts customized per category (Electronics, Fashion, Skincare)
- Auto-evaluation for readability and word count
- Fallbacks for missing product data
- Prompt engineering with Jinja templating

## ⚙️ Setup
```bash
pip install -r requirements.txt
```
Create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## 🚀 Run
```bash
python generator.py
```

## 🧪 Evaluate
```python
from evaluate.evaluate_output import evaluate_description
print(evaluate_description("<description here>"))
```

## 🧠 Design Decisions
- **Jinja2 Templates** for easy variable injection and prompt editing
- **Category-wise prompt isolation** for better tone control
- **Safe fallback rendering** for missing info edge cases
- **OpenAI GPT model** used for high-quality text generation
