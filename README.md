# DI Slam Dunks - Python Design Patterns

A comprehensive reference implementation demonstrating **Dependency Injection**, **Clean Architecture**, and **Hexagonal Architecture** in Python using FastAPI.

This project serves as a playground for myself to experiment with different design patterns and best practices in Python.

## Tech Stack

-   **Framework**: [FastAPI]
-   **Database**: PostgreSQL
-   **ORM**: [SQLAlchemy]
-   **Task Queue**: [Celery]
-   **Broker/Cache**: Redis
-   **Dependency Injection**
## Project Structure

```
,..

```

## Getting Started

### Docker Setup (Recommended)

1.  **Start the application:**
    ```bash
    docker-compose up --build
    ```

2.  **Access the services:**
    -   **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
    -   **Flower (Celery Monitor)**: [http://localhost:5555](http://localhost:5555)

### Local Development Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    uvicorn src.main:app --reload
    ```
