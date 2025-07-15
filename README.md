# 👨‍🍳 ChefGenius — Your AI-Powered Cooking Companion 🍳

ChefGenius is an AI cooking assistant built with **Streamlit**, **Google Gemini**, and **Exa** APIs. It takes your ingredients or preferences and instantly generates beautifully formatted, emoji-rich recipes along with real-world recipe links and an option to download the recipe.

---

## ✨ Features

- 🧠 **AI-Generated Recipes** using Gemini (Gemini Pro 2.5)
- 🔍 **Real-World Recipe Links** powered by Exa.ai search
- 📦 **Download Recipe** as a `.txt`,`.md`
- 🤖 Designed with human-friendly formatting (Markdown, emojis, tips)

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit
- **LLM Backend:** Google Gemini via `google.generativeai`
- **Search API:** Exa.ai for retrieving real online recipes
- **Environment:** Python 3.10+

---

## 🚀 Getting Started

### 1. Clone the Repository

- git clone https://github.com/Parneet22Singh/Recipe_creator.git
- cd Recipe_creator

### Install requirements
- pip install -r requirements.txt
  
### Setup Environment Variables
- GEMINI_API_KEY=your_gemini_api_key
- EXA_API_KEY=your_exa_api_key

### Run the app
-streamlit run app.py
### Directory Structure
.
├── app.py
├── .env
├── requirements.txt
└── README.md

## NOTE
- app.py is better in terms of user experience, but app1.py is slightly more stable. Its up to you to choose whichever verison you want to utilize.
- You might face issues (connectivity issues) with Exa.ai API requests, but not to worry, just a reload and you would be set. 

## Contribute
- Consider contributing by fine tuning the existing models to make them even more robust, or consider adding more features.
- To contrbute you can branch the repository aond push your own commits.
