from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl

from oauth_server.database import OAuthDB


class App(BaseModel):
    app_name: AnyUrl
    redirect_uri: AnyUrl


app = FastAPI()
db = OAuthDB()

@app.get("/status")
def status_check():
    return {"Hello": "World"}

@app.post("/register/")
def register(app: App):
    return app.app_name 

@app.post("/login")
def login():
    pass
