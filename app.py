from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.title = "API Videoclub"
app.description = "API que gestiona una BBDD de usuarios y películas"

app.include_router(user)

