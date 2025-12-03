from fastapi import APIRouter, HTTPException
from typing import List

from app.models import DeploymentConfig, DeploymentConfigOut
from app import database

router = APIRouter(
    prefix="/deployments",
    tags=["Lorax Deployments"],
)


@router.post("/", response_model=DeploymentConfigOut)
def create_deployment(payload: DeploymentConfig):
    deployment_id = database.create_deployment(payload.dict())
    stored = database.get_deployment(deployment_id)
    return stored


@router.get("/", response_model=List[DeploymentConfigOut])
def list_deployments():
    return database.get_all_deployments()


@router.get("/{deployment_id}", response_model=DeploymentConfigOut)
def get_deployment(deployment_id: str):
    deployment = database.get_deployment(deployment_id)
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")
    return deployment


@router.put("/{deployment_id}", response_model=DeploymentConfigOut)
def update_deployment(deployment_id: str, payload: DeploymentConfig):
    ok = database.update_deployment(deployment_id, payload.dict())
    if not ok:
        raise HTTPException(status_code=404, detail="Deployment not found")

    return database.get_deployment(deployment_id)


@router.delete("/{deployment_id}")
def delete_deployment(deployment_id: str):
    ok = database.delete_deployment(deployment_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Deployment not found")
    return {"deleted": True}

