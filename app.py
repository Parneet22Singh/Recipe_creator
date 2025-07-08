import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from agno.agent import Agent
import requests

# ----------------- Load API keys -----------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")

# ----------------- Gemini Wrapper -----------------
class GeminiChat:
    def __init__(self, model_name="models/gemini-2.5-pro", api_key=None):
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=genai.GenerationConfig(
                temperature=0.7,
                top_p=1,
                top_k=1,
                max_output_tokens=2048,
            )
        )

    def chat(self, messages):
        prompt = "\n".join([m["content"] for m in messages])
        response = self.model.generate_content(prompt)
        return response.text.strip()

# ----------------- Exa Tool -----------------
class ExaTools:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_recipes(self, query: str):
        url = "https://api.exa.ai/search"
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "query": query,
            "num_results": 5
        }
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            return f"⚠️ Could not fetch from Exa API: {e}"

        results = data.get("results", [])
        if not results:
            return []

        recipes = []
        for r in results:
            recipes.append({
                "title": r.get("title", "Untitled"),
                "url": r.get("url", "#"),
                "author": r.get("author", ""),
                "published": r.get("publishedDate", "")[:10],
                "image": r.get("image", None),
            })
        return recipes

# ----------------- Agent Setup -----------------
SYSTEM_PROMPT = """
You are ChefGenius, a culinary AI assistant.

Respond ONLY in Markdown and ALWAYS include:
- A catchy recipe title
- Ingredient list with units
- Numbered cooking steps
- Emojis for dietary/timing tags:
  ⏱️ Quick, 🍽️ Full-course, 🌱 Vegetarian, 🌿 Vegan, 🌾 Gluten-free, 🥜 Nut warnings
- Approximate nutrition per serving (kcal, protein, carbs, fat)
- Tips on substitutions, plating, storage, and wine pairings

Be friendly and concise. Adapt for user skill level and dietary restrictions.
"""

gemini = GeminiChat(api_key=GEMINI_API_KEY)
exa_tools = ExaTools(EXA_API_KEY)

agent = Agent(
    model=gemini,
    tools=[exa_tools],
    instructions=SYSTEM_PROMPT,
    markdown=True
)


def download_txt(recipe_text):
    st.download_button(
        label="📄 Download Recipe as TXT",
        data=recipe_text,
        file_name="recipe.txt",
        mime="text/plain"
    )

def download_md(recipe_text):
    st.download_button(
        label="📄 Download Recipe as MD",
        data=recipe_text,
        file_name="recipe.md",
        mime="text/markdown"
    )


# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="ChefGenius 🍳", layout="centered")
st.markdown("<h1 style='text-align:center;'>👨‍🍳 ChefGenius</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Your AI-powered cooking companion</p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("recipe_form"):
    user_query = st.text_area(
        "🥕 What ingredients and preferences do you have?",
        placeholder="e.g. I have mushrooms, garlic, pasta. Want a 20-minute vegetarian meal."
    )
    show_real = st.checkbox("🔗 Show real recipes from the web")
    submit = st.form_submit_button("🍳 Generate Recipe")

if submit:
    if not user_query.strip():
        st.warning("⚠️ Please enter something to get a recipe.")
    else:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]

        with st.spinner("👨‍🍳 ChefGenius is preparing your recipe..."):
            recipe = agent.model.chat(messages)
            st.markdown(recipe)
            download_txt(recipe)
            download_md(recipe)

        if show_real:
            with st.spinner("🔍 Searching Exa for matching real-world recipes..."):
                recipes = exa_tools.search_recipes(user_query)

                if isinstance(recipes, str):
                    # It's an error message string
                    st.error(recipes)
                elif not recipes:
                    st.info("🔍 No matching recipes found.")
                else:
                    for recipe in recipes:
                        st.markdown("---")
                        cols = st.columns([1, 3])
                        with cols[0]:
                            if recipe["image"]:
                                st.image(recipe["image"], width=120)
                            else:
                                st.write("🍽️ No Image")
                        with cols[1]:
                            st.markdown(f"### [{recipe['title']}]({recipe['url']})")
                            author_line = f"by *{recipe['author']}*" if recipe['author'] else ""
                            date_line = f" ({recipe['published']})" if recipe['published'] else ""
                            st.markdown(f"{author_line}{date_line}")

st.markdown("<hr><p style='text-align:center; color:gray;'>Made with ❤️ by Parneet</p>", unsafe_allow_html=True)
