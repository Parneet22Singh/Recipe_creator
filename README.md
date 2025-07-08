# 👨‍🍳 ChefGenius — Your AI-Powered Cooking Companion 🍳

ChefGenius is an AI cooking assistant built with **Streamlit**, **Google Gemini**, and **Exa** APIs. It takes your ingredients or preferences and instantly generates beautifully formatted, emoji-rich recipes along with real-world recipe links and an option to download the recipe.

---

## ✨ Features

- 🧠 **AI-Generated Recipes** using Gemini (Gemini Pro 2.5)
- 🔍 **Real-World Recipe Links** powered by Exa.ai search
- 📦 **Download Recipe** as a `.txt`, `.md`
- 🎨 *(Optional)*: Add AI-generated dish images (via Stability API)
- 🤖 Designed with human-friendly formatting (Markdown, emojis, tips)

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit
- **LLM Backend:** Google Gemini via `google.generativeai`
- **Search API:** Exa.ai for retrieving real online recipes
- **Image Generation (Optional):** Stability.ai API
- **Environment:** Python 3.10+

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/chef-genius.git
cd chef-genius

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

