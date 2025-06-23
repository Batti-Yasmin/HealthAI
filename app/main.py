from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routes import chat, predict, remedies, treatment, analytics, profile

app = FastAPI(title="HealthAI - Generative AI Healthcare Assistant")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Routes
app.include_router(chat.router)
app.include_router(predict.router)
app.include_router(remedies.router)
app.include_router(treatment.router)
app.include_router(analytics.router)
app.include_router(profile.router)

# Main HTML page
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
