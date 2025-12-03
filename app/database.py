from typing import Dict, Any

DEPLOYMENTS: Dict[str, Dict[str, Any]] = {}
COUNTER = 0


def create_deployment(data: Dict[str, Any]) -> str:
    """
    Creates a new deployment config and returns deployment_id.
    In future, this is where you'd call the schema/DB service.
    """
    global COUNTER
    COUNTER += 1
    deployment_id = str(COUNTER)
    DEPLOYMENTS[deployment_id] = {**data, "deployment_id": deployment_id}
    return deployment_id


def get_deployment(deployment_id: str):
    return DEPLOYMENTS.get(deployment_id)


def get_all_deployments():
    return list(DEPLOYMENTS.values())


def update_deployment(deployment_id: str, data: Dict[str, Any]) -> bool:
    if deployment_id not in DEPLOYMENTS:
        return False
    DEPLOYMENTS[deployment_id].update(data)
    return True


def delete_deployment(deployment_id: str) -> bool:
    if deployment_id in DEPLOYMENTS:
        del DEPLOYMENTS[deployment_id]
        return True
    return False
