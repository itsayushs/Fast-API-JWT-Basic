from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from service.auth.auth_handler import signJWT

router = APIRouter()

@router.get("/new", response_description="Use this to get a token")
async def get_sre_package_for_specific_month(request: Request):
    TOKEN = signJWT("backend")
    return JSONResponse(status_code=status.HTTP_200_OK, content=TOKEN)