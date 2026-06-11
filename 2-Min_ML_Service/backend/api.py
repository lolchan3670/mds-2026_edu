from pathlib import Path
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from backend.ml.train import train_model

app = FastAPI()


class TrainRequest(BaseModel):
    filename: str
    model_name: str
    train_size: float = 0.8


@app.post("/train/logistic")
def train_logistic( req: TrainRequest, background_tasks: BackgroundTasks):

    path = Path("data") / req.filename

    if not path.is_file():
        raise HTTPException(status_code=404, detail="Data file not found")

    background_tasks.add_task(train_model, req.filename, req.model_name, "logistic", req.train_size)
    return { "message": "Logistic Regression training started"}


@app.post("/train/random_forest")
def train_random_forest( req: TrainRequest, background_tasks: BackgroundTasks):

    path = Path("data") / req.filename

    if not path.is_file():
        raise HTTPException( status_code=404, detail="Data file not found")

    background_tasks.add_task(train_model, req.filename, req.model_name, "random_forest", req.train_size)
    return {"message": "Random Forest training started"}