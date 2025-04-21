from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()
logger = logging.getLogger("uvicorn")

class Metric(BaseModel):
    student_id: int
    score: float

metrics = []

@app.post("/metrics")
def add_metric(metric: Metric):
    metrics.append(metric)
    logger.info(f"Added metric for student {metric.student_id}")
    return {"message": "Metric added successfully"}

@app.get("/metrics")
def get_metrics():
    return metrics

@app.get("/metrics/average")
def get_average():
    if not metrics:
        return {"average": 0}
    return {"average": sum(m.score for m in metrics) / len(metrics)}
