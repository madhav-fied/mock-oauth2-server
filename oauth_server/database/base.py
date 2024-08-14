import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import date, timedelta

from oauth_server.database.utils import generate_random_uuid
from oauth_server.database.models import ClientSchema, AuthzSchema


DB_URL = os.getenv("DB_URL","postgresql+asyncpg://testusr:123@localhost/testdb")

class OAuthClientDB():
    def __init__(self):
        self.db_engine = create_async_engine(DB_URL, echo=True)
    
    async def create_tables(self):
        async with self.db_engine.begin() as connection:
            await connection.run_sync(ClientSchema.metadata.create_all)

    async def get_client_by_id(self, *, client_id):
        async with AsyncSession(self.db_engine) as a_session:
            statement = select(ClientSchema).filter_by(client_id=client_id)

            result = await a_session.execute(statement=statement)
            client = result.scalars().first()
        
            return client

    async def create_client(self, *, client_id, redirect_uri):
        new_client = ClientSchema(client_id=client_id, redirect_uri=redirect_uri, client_secret=generate_random_uuid())
        async with AsyncSession(engine=self.db_engine) as a_session:
            async with a_session.begin():
                try:
                    await a_session.add(new_client)
                except SQLAlchemyError as e:
                    await a_session.rollback()
                    raise Exception(f"Some error occured when inserting {new_client} to DB: {e}")
                else:
                    await a_session.commit()
        return new_client
        

class OAuthAuthzCodesDB():
    def __init__(self):
        self.db_engine = create_async_engine(DB_URL, echo=True)
        await self.create_tables()

    async def create_tables(self):
        async with self.db_engine.begin() as connection:
            await connection.run_sync(AuthzSchema.metadata.create_all)
    
    async def get_authz_code_by_client_id(self, *, client_id):
        async with AsyncSession(self.db_engine) as a_session:
            statement = select(AuthzSchema).filter_by(client_id)

            result = await a_session.execute(statement=statement)
            client = result.scalars().first()

            if isinstance(client, AuthzSchema):
                return client
            else:
                client = await self.create_authz_code(client_id=client_id)
                return client
    
    async def create_authz_code(self, *, client_id, validity_days = 30):
        new_expiry_date = date.today() + timedelta(validity_days)
        new_auth_entry = AuthzSchema(client_id=client_id, authz_code=generate_random_uuid(), expiry=new_expiry_date, is_expired=False)
        async with AsyncSession(self.db_engine) as a_session:
            async with a_session.begin():
                try:
                    await a_session.add(new_auth_entry)
                except SQLAlchemyError as e:
                    await a_session.rollback()
                    raise Exception(f"Some error occured when inserting {new_auth_entry} to DB: {e}")
                else:
                    await a_session.commit()
        return new_auth_entry
        