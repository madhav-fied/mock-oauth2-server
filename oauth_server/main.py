from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, AnyUrl
from oauth_server.models import (OAuthClientRegistration, OAuthClientLoginAttempt)

app = FastAPI()
templates = Jinja2Templates(directory="htmx-templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def status_check():
    return "OK"

@app.get("/register/", response_class=HTMLResponse)
def get_register_form(request: Request):
    # returns html for login form
    return templates.TemplateResponse(request=request, name="register-app.html")

@app.post("/register/", response_class=HTMLResponse)
def register_app(app: OAuthClientRegistration):
    # get details from form and return a modal with client secret
    # error details in modal
    print(app)
    pass
    


@app.post("/login")
def login(app: OAuthClientLoginAttempt):
    pass
