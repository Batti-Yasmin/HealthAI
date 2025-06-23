import os
import google.generativeai as genai

# Load Gemini API key from environment variable or replace with your key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or "your-api-key-here"

genai.configure(api_key=GOOGLE_API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
