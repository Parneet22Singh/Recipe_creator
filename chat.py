import google.generativeai as genai

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
            ),
        )

    def chat(self, messages):
        prompt = "\n".join([m["content"] for m in messages])
        response = self.model.generate_content(prompt)
        return response.text.strip()
