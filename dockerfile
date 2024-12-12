FROM python:3.12-slim

WORKDIR /app

RUN pip3 install poetry

COPY /pyproject.toml /app/

RUN poetry config virtualenvs.create false &&  poetry install --no-root --no-dev

COPY . /app

EXPOSE 7979

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7979"]