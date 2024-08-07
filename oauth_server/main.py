from fastapi import FastAPI

from pydantic import BaseModel, AnyUrl


class App(BaseModel):
    app_name: AnyUrl
    redirect_uri: AnyUrl


app = FastAPI()

@app.get("/status")
def read_root():
    return {"Hello": "World"}

@app.post("/register/")
def register(app: App):
    return app.app_name 

@app.post("/login")
def login():
    pass



