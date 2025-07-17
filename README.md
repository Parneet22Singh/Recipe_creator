# **ChefGenius 🍳 - Recipe Generator with AI and Real Recipes**

**ChefGenius** is a Flask-based web application that allows users to input their ingredients or preferences, and get an AI-generated recipe along with real-world recipes. The real recipes are automatically shown for the user's convenience.

---

## **Features:**
- **AI-generated recipe** based on user input (ingredients or preferences).
- **Real-world recipes** fetched from an external API (always displayed with the AI recipe).
- **Responsive design** with modern UI elements (using Tailwind CSS).
- Option to **download the recipe** as a `.txt` or `.md` file.
- **Dark mode** and **light mode** toggle for better user experience.

---

## **Technologies Used:**
- **Python** (Flask framework)
- **Tailwind CSS** (for styling and responsive design)
- **Alpine.js** (for handling dark mode toggle)
- **External Recipe API** for fetching real-world recipes.
- **Gemini** (for generating AI-based recipes).

---

## **Requirements:**

- Python 3.7 or higher.
- Pip (for installing Python packages).

### **Install Dependencies:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Parneet22Singh/Recipe_creator.git
   cd Recipe_creator
2. Install the required dependencies:
    - pip install -r requirements.txt
   
3. Set up environment variables:
   - GEMINI_API_KEY=your_gemini_api_key
   - EXA_API_KEY=your_exa_api_key
     
## Start the flask server:
   - python main.py
     
## App features:
Homepage:

The user can input ingredients or meal preferences (e.g., "mushrooms, garlic, pasta, 20-minute vegetarian meal").

Upon submission, the page displays:

The AI-generated recipe based on the input.

A list of real-world recipes fetched from an API (always displayed).

Users can download the recipe as a .txt or .md file.

Real Recipe Display:

Real recipes are automatically fetched and displayed, even if the user does not check any checkbox (they are always shown).

Dark Mode / Light Mode Toggle:

The app supports both dark mode and light mode. The toggle is handled using Alpine.js and Tailwind CSS.

## File Structure
.
├── main.py              # Main Flask application
├── requirements.txt     # Required Python packages
├── config.py            # Configuration for your app (API keys, etc.)
├── agent.py             # Logic for interacting with AI and APIs
│── chat.py
├── templates/           # HTML files
│   └── index.html       # Main template for the homepage
├── static/              # Static assets (CSS, images, etc.)
│   └── chef.jpg         # Example image for the header
└── .env                 # Environment variables (API keys)


