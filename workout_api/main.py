from fastapi import FastAPI
from workout_api.routers import api_router
import uvicorn

app = FastAPI(
    title="Api de Atletas",
    description="API de controle de treinos e centros de treinamento.",
    version="1.0.0",
)

app.include_router(api_router)


def run():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    run()