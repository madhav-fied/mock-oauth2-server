from pydantic import BaseModel, AnyHttpUrl, validator
import re

# oauth client register
# oauth client login
# oauth client getting access token
# oauth accessing the resource

class OAuthClientRegistration(BaseModel):
    client_id: AnyHttpUrl
    redirect_url: AnyHttpUrl

    @validator('redirect_url')
    def redirect_url_should_be_https(self, given_value):
        assert re.search("^https:", given_value), 'rediret must support https endpoint'

class OAuthClientLoginAttempt(BaseModel):
    client_id: AnyHttpUrl
    response_type: "code"
    redirect_url: AnyHttpUrl
    scope: str
    state: str

    @validator('redirect_url')
    def redirect_url_should_be_https(self, given_value):
        assert re.search("^https:", given_value), 'rediret must support https endpoint'

class OAuthClientAccessResource(BaseModel):
    access_token: str
    scope: str
    client_id: AnyHttpUrl

class OAuthClientAuthzCodeExchange(BaseModel):
    grant_type: "authorization_code"
    code: str
    redirect_url: AnyHttpUrl
    client_id: AnyHttpUrl
    client_secret: str

