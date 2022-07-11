from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from routes.token import router as token_router
from routes.locked import router as locked_router

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(token_router, tags=["Token"], prefix="/token")
api.include_router(locked_router, tags=["Posts"], prefix="/posts")



if __name__ == "__main__":
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        reload=True,
        port=3000,
    )