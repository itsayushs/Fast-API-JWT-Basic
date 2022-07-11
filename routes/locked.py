from fastapi import APIRouter, Body, Depends, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from service.auth.auth_bearer import JWTBearer
from service.auth.auth_handler import signJWT


router = APIRouter()

@router.get("/", dependencies=[Depends(JWTBearer())], response_description="Locked GET Route")
async def get_sre_package_for_specific_month(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": "hello-world"})