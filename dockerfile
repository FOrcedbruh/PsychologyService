FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install poetry

COPY /pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

COPY . .

EXPOSE 7979

CMD ["uvicorn", "main:app"]