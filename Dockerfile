FROM python:3.10

WORKDIR /runner_project

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry install

COPY README.md TODO.md ./

COPY app ./app

COPY static ./static

COPY templates ./templates

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]