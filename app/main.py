from fastapi import FastAPI

from app.routers.movies import movies_router

app = FastAPI(title='Cinemapedia', version='0.0.1')

app.include_router(movies_router)