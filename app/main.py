from fastapi import FastAPI
from .routers import users, questions

app = FastAPI()

app.include_router(users.router)
app.include_router(questions.router)
