from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.apps.auth.utils import verify_token
from src.apps.common.domain.ports.use_case import UseCasePort
from src.apps.common.utils.api import Request
from src.containers import AppContainer

router = APIRouter()


@router.get('/me', dependencies=[Depends(verify_token)])
@inject
def me(
    request: Request,
    use_case: UseCasePort = Depends(Provide[AppContainer.auth_package.get_current_user_use_case])
):
    return use_case.execute(request.user_id) 