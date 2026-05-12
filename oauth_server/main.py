from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from oauth_server.models import OAuthClientRegistration, OAuthClientLoginAttempt
from oauth_server.database import OAuthClientDB
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

app.mount("/register/form", StaticFiles(directory="static/register/", html=True), name="register")

@app.post("/register/", response_class=HTMLResponse)
async def register_app(client: OAuthClientRegistration):
    # get details from form and return a modal with client secret
    # error details in modal as response = 422   
    clientDB = OAuthClientDB()
    clientDB.create_client(client_id=client.client_id, redirect_uri=client.redirect_url)
    return "Done"
    


@app.post("/login")
def login(app: OAuthClientLoginAttempt):
    pass
