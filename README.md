## Development Setup

### Virtual Environment Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start
    Start Docker Desktop:
   - Open Docker.app from Applications
   - Wait for it to start (whale icon in menu bar)

3. Run the application:
```bash
docker-compose up
```

The application will be available at:
- API: http://localhost:8000
# - Database: localhost:5432
# - Redis: localhost:6379
- Flower (Celery monitoring): http://localhost:5555


## About

This repository is intended to serve as a resource for Python developers who are interested in learning about dependency injection and how it can be applied in their projects. Each snippet demonstrates a specific aspect of DI, along with explanations and usage examples.

