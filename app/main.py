from fastapi import FastAPI

from app.routers.movies import movies_router
from app.models.movie import Movie
from app.config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Cinemapedia', version='0.0.1')

app.include_router(movies_router)