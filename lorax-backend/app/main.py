from fastapi import FastAPI
from app.routers import deployments, infer

app = FastAPI(title="Lorax Deployment Service")

app.include_router(deployments.router)
app.include_router(infer.router)


@app.get("/")
def root():
    return {"status": "ok", "service": "lorax-backend"}
