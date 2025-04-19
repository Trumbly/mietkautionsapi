# Mietkautionstool

A FastAPI-based application for managing rental deposits.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application in development mode:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation at http://localhost:8000/docs
- ReDoc documentation at http://localhost:8000/redoc

## Running Tests

To run the tests:

```bash
pytest
```

## Project Structure

```
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── router.py
│   ├── core/
│   │   └── config.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```
