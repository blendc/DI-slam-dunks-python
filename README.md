# DI Slam Dunks - Python Design Patterns

A comprehensive reference implementation demonstrating **Dependency Injection**, **Clean Architecture**, and **Hexagonal Architecture** in Python using FastAPI.

This project serves as a practical resource for developers looking to master advanced Python design patterns and build scalable, maintainable applications.

## 🚀 Features

-   **Dependency Injection**: robust DI implementation using `dependency-injector`.
-   **Clean Architecture**: Separation of concerns with distinct layers (Domain, Application, Infrastructure).
-   **Modern Stack**: Built with FastAPI, SQLAlchemy 2.0, and Pydantic v2.
-   **Asynchronous Processing**: Background task handling with Celery and Redis.
-   **Containerization**: Full Docker and Docker Compose support for easy deployment.

## 🛠️ Tech Stack

-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Database**: PostgreSQL
-   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Async)
-   **Task Queue**: [Celery](https://docs.celeryq.dev/)
-   **Broker/Cache**: Redis
-   **Dependency Injection**: [dependency-injector](https://python-dependency-injector.ets-labs.org/)

## 📂 Project Structure

```
src/
├── apps/               # Application & Domain Layer
│   ├── auth/           # Auth Module (Domain, Ports, Use Cases)
│   ├── common/         # Shared Utilities & Interfaces
│   └── redis/          # Redis Module
├── infrastructure/     # Infrastructure Layer (Drivers, Config, DB)
├── containers.py       # Dependency Injection Containers
└── main.py             # Application Entry Point
```

## ⚡ Getting Started

### Prerequisites

-   Docker & Docker Compose
-   Python 3.11+ (for local development)

### 🐳 Docker Setup (Recommended)

1.  **Start the application:**
    ```bash
    docker-compose up --build
    ```

2.  **Access the services:**
    -   **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
    -   **Flower (Celery Monitor)**: [http://localhost:5555](http://localhost:5555)

### 💻 Local Development Setup

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

## 📖 Usage

The application exposes a REST API documented via Swagger UI.

-   **Authentication**: The `auth` module provides endpoints for user authentication.
-   **Dependency Injection**: Check `src/containers.py` to see how services are wired.
-   **Domain Logic**: Business logic resides in `src/apps/*/domain`, isolated from frameworks.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
