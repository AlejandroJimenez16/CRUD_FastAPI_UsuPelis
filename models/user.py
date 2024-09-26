from sqlalchemy import Table, Column, ForeignKey
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import engine

customers = Table('customers', meta, 
            Column("id", Integer, primary_key=True),
            Column("name", String(255)),
            Column("email", String(255)),
            Column("password", String(255)),
            Column("phone", Integer),
            Column("create_at", DateTime),
            Column("update_date", DateTime)
        )

movies = Table('movies', meta, 
            Column("id", Integer, primary_key=True),
            Column("name", String(255)),
            Column("genre", String(255)),
            Column("year", Integer),
            Column("create_at", DateTime),
            Column("update_date", DateTime)
        )

movieStatus = Table('movieStatus', meta, 
            Column("id", Integer, primary_key=True),
            Column("status", String(255)),
            Column("create_at", DateTime),
            Column("update_date", DateTime)
        )

userMovies = Table('userMovies', meta,
            Column("id", Integer, primary_key=True),
            Column("idCustomer", Integer, ForeignKey("customers.id")),
            Column("idMovie", Integer, ForeignKey("movies.id")),
            Column("idStatus", Integer, ForeignKey("movieStatus.id")),
            Column("create_at", DateTime),
            Column("update_date", DateTime)
        )

meta.create_all(engine)