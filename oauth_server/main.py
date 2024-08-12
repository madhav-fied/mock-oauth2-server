from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, AnyUrl
from oauth_server.models import (OAuthClientRegistration, OAuthClientLoginAttempt)

app = FastAPI()
templates = Jinja2Templates(directory="htmx-templates")

@app.get("/status")
def status_check():
    return "OK"

@app.get("/register/", response_class=HTMLResponse)
def get_register_form():
    # returns html for login form
    pass

@app.post("/register/", response_class=HTMLResponse)
def register_app(app: OAuthClientRegistration):
    # get details from form and return a modal with client secret
    # error details in modal
    pass


@app.post("/login")
def login(app: OAuthClientLoginAttempt):
    pass
