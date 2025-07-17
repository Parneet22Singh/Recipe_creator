from flask import Flask, request, send_file
import io
from ui import setup_routes

app = Flask(__name__)
setup_routes(app)

@app.post("/download/txt")
def download_txt():
    recipe_text = request.form.get("recipe_text", "")
    return send_file(
        io.BytesIO(recipe_text.encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name="recipe.txt"
    )

@app.post("/download/md")
def download_md():
    recipe_text = request.form.get("recipe_text", "")
    return send_file(
        io.BytesIO(recipe_text.encode("utf-8")),
        mimetype="text/markdown",
        as_attachment=True,
        download_name="recipe.md"
    )

if __name__ == "__main__":
    app.run(debug=True)
