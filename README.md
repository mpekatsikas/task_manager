# Task Manager App

A simple Task Manager application built with **FastAPI** for the backend and **React** for the frontend. The app allows users to **create, read, update, and delete (CRUD)** tasks. It runs using **Docker and Docker Compose**.

## Features
- 🏗 Full CRUD functionality for managing tasks
- 🚀 FastAPI backend with SQLAlchemy and PostgreSQL
- ⚡ React frontend using Axios for API requests
- 🐳 Containerized with Docker for easy deployment

---

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 📦 Setup & Installation

### 1. Clone the repository
```sh
git clone repo
cd task_manager
```

### 2. Setup Backend
```sh
uvicorn backend.app.main:app --host=0.0.0.0 --port 8080
```

Once running, visit:

Swagger UI: http://0.0.0.0:8080/docs
ReDoc: http://0.0.0.0:8080/redoc


### 3. Setup Frontend
```sh
npm start
```
The React app will be available at http://localhost:3000.

### 4. Build and run with Docker
```sh
docker-compose up --build
```
The backend will be available at http://0.0.0.0:8080/, and the frontend at http://localhost:3000.