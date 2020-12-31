import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)
from databases import Database


#from app.api.credentials import server, username, password, your_database

DATABASE_URI = os.getenv('DATABSE_URI')

#DATABASE_URI = f'{server}://{username}:{password}@localhost/{your_database}'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

database = Database(DATABASE_URL)
