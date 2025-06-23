# 🧠 HealthAI - Intelligent Healthcare Assistant

HealthAI is a generative AI-powered healthcare assistant that uses **IBM Granite** and **Gemini AI** to provide:

### ✅ Features:
- 🧠 **Patient Chat System** – Ask medical questions and get AI advice.
- 🩺 **Symptom Identifier** – Predict possible diseases from symptoms.
- 🌿 **Home Remedies** – Natural remedies based on user-entered conditions.
- 💊 **Treatment Plan Generator** – Personalized plans based on condition, age, gender.
- 📊 **Health Analytics Dashboard** – Visualize health data + AI insights.
- 👤 **Profile Manager** – Manage patient details easily.
- 🔁 **No Login Required** – Anyone can use it freely.

---

### 🛠 Built With:
- `FastAPI` + `Jinja2` for backend + frontend
- `transformers` (Hugging Face) – IBM Granite model
- `google-generativeai` – Gemini Pro integration
- `torch`, `pydantic` for AI + validation

---

### 🚀 Live Demo (after deployment)
→ [Coming soon on Hugging Face Spaces](https://huggingface.co/spaces)

---

### 📂 Run Locally:
```bash
uvicorn app.main:app --reload
