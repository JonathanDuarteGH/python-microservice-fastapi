from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

from app.api.credentials import server, username, password, your_database

DATABASE_URL = f'{server}://{username}:{password}@localhost/{your_database}'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)