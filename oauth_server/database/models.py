from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date

Base = declarative_base()

class ClientSchema(Base):
    __tablename__ = 'oauth_client'

    client_id = Column(String, unique=True, primary_key=True, nullable=False)
    client_secret = Column(String, unique=True, nullable=False)
    redirect_uri = Column(String, nullable=False)

    def __repr__(self):
        return f"Client(id={self.client_id}, redirect_uri={self.redirect_uri}, secret={self.client_secret})"

class AuthzSchema(Base):
    __tablename__ = 'oauth_secret_store'

    client_id = Column(String, unique=True, primary_key=True, nullable=False)
    authz_code = Column(String, unique=True, nullable=False)
    expiry = Column(Date, nullable=False)
    is_expired = Column(Boolean, nullable=False)
    
    def __repr__(self):
        return f"Authz(client_id={self.client_id}, auth_code={self.authz_code}, expiry={self.expiry}, is_expired={self.is_expired})"


