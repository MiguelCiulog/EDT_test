from fastapi import FastAPI

from src.api.v1.api import api_router as v1_router

app = FastAPI()


@app.get("/health/")
async def check_health():
    return "Server is active"


app.include_router(v1_router)
