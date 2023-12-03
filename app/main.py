
from app.model.model import __version__ as model_version
from app.model.model import process_image, convert_to_lines
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}
