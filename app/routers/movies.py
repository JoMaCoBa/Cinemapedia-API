from fastapi import APIRouter

from app.schemas.movie import Movie

movies_router = APIRouter(prefix="/movies", tags=['Movies'])

@movies_router.get('')
def get_movies():
    """TODO: Create function to obtain Movies to the DataBase"""
    pass

@movies_router.post('')
def create_movie(movie: Movie):
    """TODO: Create function to create a new record of movie in the DataBase"""
    pass

@movies_router.put('')
def update_movie(movie: Movie):
    """TODO: Create function to update a movie information"""
    pass

@movies_router.delete('')
def delete_movie(id: int):
    """TODO: Create a function to delete a movie by ID"""
    pass