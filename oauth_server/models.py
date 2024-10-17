from pydantic import BaseModel, AnyHttpUrl, validator
from typing_extensions import Annotated

from fastapi import Form

import re

class OAuthClientRegistration(BaseModel):
    client_id: Annotated[AnyHttpUrl, Form()]
    redirect_url: Annotated[AnyHttpUrl, Form()]

    @validator('redirect_url')
    def redirect_url_should_be_https(cls, given_value):
        assert re.search("^https:", given_value), 'rediret must support https endpoint'

class OAuthClientLoginAttempt(BaseModel):
    client_id: AnyHttpUrl
    response_type: str
    redirect_url: AnyHttpUrl
    scope: str
    state: str

    @validator('redirect_url')
    def redirect_url_should_be_https(cls, given_value):
        assert re.search("^https:", given_value), 'rediret must support https endpoint'

class OAuthClientAccessResource(BaseModel):
    access_token: str
    scope: str
    client_id: AnyHttpUrl

class OAuthClientAuthzCodeExchange(BaseModel):
    grant_type: str
    code: str
    redirect_url: AnyHttpUrl
    client_id: AnyHttpUrl
    client_secret: str

