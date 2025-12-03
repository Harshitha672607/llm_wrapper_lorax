from fastapi import APIRouter

router = APIRouter(
    prefix="/infer",
    tags=["Inference"],
)


@router.post("/")
def infer(question: str):
    # Later you will call the Lorax service here (inside cluster)
    # using LORAX_URL env or a Kubernetes service like http://lorax.lorax.svc.cluster.local
    return {"message": "Inference endpoint not wired yet", "question": question}
