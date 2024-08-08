from pydantic import BaseModel

# oauth client register
# oauth client login
# oauth client getting access token
# oauth accessing the resource

class OAuthClientRegistration(BaseModel):
    pass

class OAuthClientLoginAttempt(BaseModel):
    pass

class OAuthClientAccessResourc(BaseModel):
    pass

class OAuthClientAuthzCodeExchange(BaseModel):
    pass

