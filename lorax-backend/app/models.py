from pydantic import BaseModel
from typing import Optional


class DeploymentConfig(BaseModel):
    # matches your schema attributes
    name: str = "lorax"
    namespace: str = "lorax"
    model_id: str               # e.g. "yahma/llama-7b-hf"

    cpu: str = "4"              # "4"
    memory: str = "24Gi"        # "24Gi"
    gpu: int = 1                # 1

    hf_token_name: str = "hf-token"
    hf_token_key: str = "token"

    node_name: Optional[str] = "gpunode2"
    image: Optional[str] = "ghcr.io/predibase/lorax:0.4.0"
    description: Optional[str] = None


class DeploymentConfigOut(DeploymentConfig):
    deployment_id: str          # primary key used in your schema
