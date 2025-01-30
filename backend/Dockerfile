# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app
#COPY .git .git

COPY backend/poetry.lock poetry.lock
COPY backend/pyproject.toml pyproject.toml

# Install system dependencies (if needed for cryptography)
RUN apt-get update && apt-get install -y gcc libssl-dev

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies with Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

# Copy the backend application code
COPY . .
