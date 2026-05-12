from pydantic import BaseModel, AnyHttpUrl, field_validator

import re

class OAuthClientRegistration(BaseModel):
    client_id: AnyHttpUrl
    redirect_url: AnyHttpUrl

    @field_validator('redirect_url')
    @classmethod
    def redirect_url_should_be_https(cls, given_value: AnyHttpUrl):
        assert re.search("^https:", str(given_value)), 'redirect must support https endpoint'
        return given_value

class OAuthClientLoginAttempt(BaseModel):
    client_id: AnyHttpUrl
    response_type: str
    redirect_url: AnyHttpUrl
    scope: str
    state: str

    @field_validator('redirect_url')
    @classmethod
    def redirect_url_should_be_https(cls, given_value: AnyHttpUrl):
        assert re.search("^https:", str(given_value)), 'redirect must support https endpoint'
        return given_value

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

