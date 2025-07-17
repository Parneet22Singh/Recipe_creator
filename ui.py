from flask import render_template, request
from agent import get_recipe, get_real_recipes
from config import SYSTEM_PROMPT

def setup_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def index():
        recipe = None
        error = None
        real_recipes = []
        show_real = True  # Always show real recipes

        if request.method == "POST":
            user_input = request.form.get("ingredients", "").strip()

            if not user_input:
                error = "⚠️ Please enter some ingredients or preferences."
            else:
                try:
                    # Get the AI-generated recipe
                    recipe = get_recipe(user_input)

                    # Always get real recipes
                    real_recipes = get_real_recipes(user_input)

                except Exception as e:
                    error = f"❌ AI Service Error: {e}"

        return render_template(
            "index.html",
            recipe=recipe,
            error=error,
            real_recipes=real_recipes,  # Always pass real recipes
            show_real=show_real  # Optional: You can keep this if you want to track state in the frontend
        )
