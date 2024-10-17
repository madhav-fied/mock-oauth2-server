from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, AnyUrl
from oauth_server.models import (OAuthClientRegistration, OAuthClientLoginAttempt)

from typing import Annotated

app = FastAPI()

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

app.mount("/register/", StaticFiles(directory="static/register/", html=True), name="register")

@app.post("/register/", response_class=HTMLResponse)
async def register_app(client: Annotated[str, Form()], redirect_url: Annotated[str, Form()]):
    # get details from form and return a modal with client secret
    # error details in modal
    registered = OAuthClientRegistration(client_id=client, redirect_url=redirect_url)
    
    print(client)
    print(redirect_url)
    # register with backend
    return "Done"
    


@app.post("/login")
def login(app: OAuthClientLoginAttempt):
    pass
