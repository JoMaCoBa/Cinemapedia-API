# Movie API

This repository contains a Movie API built with FastAPI, featuring authentication, CRUD operations, and database management.

## Features

- **Authentication**: Secure access to the API with user authentication.
- **CRUD Operations**: Create, read, update, and delete movie records.
- **Database Management**: Efficient handling of movie data using a relational database.
- **FastAPI Framework**: Leveraging FastAPI for high performance and ease of development.
- **Validation and Serialization**: Ensuring data integrity and consistency.

## Endpoints

- **POST /auth/signup**: Register a new user.
- **POST /auth/login**: Authenticate and obtain a token.
- **GET /movies**: Retrieve a list of all movies.
- **GET /movies/{id}**: Retrieve a single movie by its ID.
- **POST /movies**: Add a new movie to the collection.
- **PUT /movies/{id}**: Update an existing movie.
- **DELETE /movies/{id}**: Delete a movie by its ID.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- SQLAlchemy (or your preferred ORM)
- A relational database (e.g., PostgreSQL, MySQL, SQLite)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-api.git
    cd movie-api
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the database settings in the `.env` file.

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

5. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
