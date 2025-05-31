from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from apps.auth.utils import verify_token
from apps.common.domain.ports.use_case import UseCasePort
from apps.common.utils.api import Request
from src.containers import AppContainer

router = APIRouter()


@router.get('/me', dependencies=[Depends(verify_token)])
@inject
def me(
    request: Request,
    use_case: UseCasePort = Depends(Provide[AppContainer.auth_package.get_current_user_use_case])
):
    return use_case.execute(request.user_id) 