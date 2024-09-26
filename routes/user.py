from fastapi import APIRouter, status, HTTPException
from config.db import conexion
from models.user import customers
from models.user import movies
from models.user import movieStatus
from models.user import userMovies
from schemas.user import Customer, Movie, MovieStatus, UserMovies
from cryptography.fernet import Fernet
from sqlalchemy.exc import IntegrityError
from datetime import datetime

user = APIRouter()

key = Fernet.generate_key()

f = Fernet(key)

# GET 
@user.get('/customer', tags=["Customers"])
def get_customer():
    try:
        valores = []
        for filas in conexion.execute(customers.select()).fetchall():
            dic = {
                "id": filas.id,
                "name": filas.name,
                "email": filas.email,
                "password": filas.password,
                "phone": filas.phone,
                "create_at": filas.create_at,
                "update_date": filas.update_date
            }
            valores.append(dic)
        return valores
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")    

@user.get('/movies', tags=["Movies"])
def get_movie():
    try:
        valores = []
        consulta = conexion.execute(movies.select()).fetchall()
        for filas in consulta:
            dic = {
                "id": filas.id,
                "name": filas.name,
                "genre": filas.genre,
                "year": filas.year,
                "create_at": filas.create_at,
                "update_date": filas.update_date
            } 
            valores.append(dic)
        return valores
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 


@user.get('/movieStatus', tags=["MovieStatus"])
def get_movieStatus():
    try:
        valores = []
        consulta = conexion.execute(movieStatus.select()).fetchall()
        for filas in consulta:
            dic = {
                "id": filas.id,
                "status": filas.status,
                "create_at": filas.create_at,
                "update_date": filas.update_date
            } 
            valores.append(dic)
        return valores
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

@user.get('/userMovies', tags=["UserMovies"])
def get_userMovie():
    try:
        valores = []
        consulta = conexion.execute(userMovies.select()).fetchall()
        for filas in consulta:
            dic = {
                "id": filas.id,
                "idCustomer": filas.idCustomer,
                "idMovie": filas.idMovie,
                "idStatus": filas.idStatus,
                "create_at": filas.create_at,
                "update_date": filas.update_date
            } 
            valores.append(dic)
        return valores
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

# POST
@user.post('/customer', tags=["Customers"])
def post_customer(customer: Customer):
    try:
        # Realizar la inserción en la base de datos
        new_customer = {
            "name": customer.name,
            "email": customer.email,
            "password": f.encrypt(customer.password.encode('utf-8')),
            "phone": customer.phone,
            "create_at": datetime.now() 
        }
        
        conexion.execute(customers.insert().values(new_customer))        
        conexion.commit()
        return "Inserción realizada correctamente"
    
    except Exception as e:
        # Manejar cualquier otro error interno
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
           
@user.post('/movies', tags=["Movies"])
def post_movie(movie: Movie):
    try:
        new_movie = {
            "name": movie.name, 
            "genre": movie.genre, 
            "year": movie.year,
            "create_at": datetime.now() 
        }
        conexion.execute(movies.insert().values(new_movie))
        conexion.commit()
        return "Insercion realizada correctamente"

    except Exception:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@user.post('/movieStatus', tags=["MovieStatus"])
def post_movieStatus(status: MovieStatus):
    try:
        new_movieStatus = {
            "id": status.id, 
            "status": status.status,
            "create_at": datetime.now() 
        }
        conexion.execute(movieStatus.insert().values(new_movieStatus))
        conexion.commit()
        return "Insercion realizada correctamente"
    except Exception as e:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@user.post('/userMovies', tags=["UserMovies"])
def post_userMovie(userMovie: UserMovies):
    try:
        new_userMovie = {
            "idCustomer": userMovie.idCustomer, 
            "idMovie": userMovie.idMovie, 
            "idStatus": userMovie.idStatus,
            "create_at": datetime.now() 
        }
        conexion.execute(userMovies.insert().values(new_userMovie))
        conexion.commit()
        return "Insercion realizada correctamente"
    except Exception as e:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

# PUT
@user.put('/customer', tags=["Customers"])
def update_customer(id: int, customer: Customer):
    try:
        # Preparamos los campos a actualizar
        update_values = {}

        if customer.name:
            update_values["name"] = customer.name
        if customer.email:
            update_values["email"] = customer.email
        if customer.password:
            update_values["password"] = f.encrypt(customer.password.encode('utf-8'))
        if customer.phone:
            update_values["phone"] = customer.phone
        if customer.update_date:
            update_values["update_date"] = datetime.now()

        # Actualizamos solo los campos proporcionados
        result = conexion.execute(customers.update().values(**update_values).where(customers.c.id == id))
        conexion.commit()

        # Verificamos si se encontró el cliente para actualizar
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id: {id} no encontrado")

        return "Actualizado"
    except IntegrityError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

@user.put('/movies', tags=["Movies"])
def update_movie(id: int, movie: Movie):
    try:
        # Preparamos los campos a actualizar
        update_values = {}

        if movie.name:
            update_values["name"] = movie.name
        if movie.genre:
            update_values["genre"] = movie.genre
        if movie.year:
            update_values["year"] = movie.year
        if movie.update_date:
            update_values["update_date"] = datetime.now()

        # Actualizamos solo los campos proporcionados
        result = conexion.execute(movies.update().values(**update_values).where(movies.c.id == id))
        conexion.commit()

        # Verificamos si se encontró el cliente para actualizar
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id: {id} no encontrado")

        return "Actualizado"
    except IntegrityError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

@user.put('/movieStatus', tags=["MovieStatus"])
def update_movieStatus(id: int, status: MovieStatus):
    try:
        # Preparamos los campos a actualizar
        update_values = {}

        if status.id:
            update_values["id"] = status.id
        if status.status:
            update_values["status"] = status.status
        if status.update_date:
            update_values["update_date"] = datetime.now()

        # Actualizamos solo los campos proporcionados
        result = conexion.execute(movieStatus.update().values(**update_values).where(movieStatus.c.id == id))
        conexion.commit()

        # Verificamos si se encontró el cliente para actualizar
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id: {id} no encontrado")

        return "Actualizado"
    except IntegrityError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

@user.put('/userMovies', tags=["UserMovies"])
def update_userMovie(id: int, userMovie: UserMovies):
    try:
        # Preparamos los campos a actualizar
        update_values = {}

        if userMovie.idCustomer:
            update_values["idCustomer"] = userMovie.idCustomer
        if userMovie.idMovie:
            update_values["idMovie"] = userMovie.idMovie
        if userMovie.idStatus:
            update_values["idStatus"] = userMovie.idStatus
        if userMovie.update_date:
            update_values["update_date"] = datetime.now()

        # Actualizamos solo los campos proporcionados
        result = conexion.execute(userMovies.update().values(**update_values).where(userMovies.c.id == id))
        conexion.commit()

        # Verificamos si se encontró el cliente para actualizar
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id: {id} no encontrado")

        return "Actualizado"
    except IntegrityError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor") 

# DELETE
@user.delete('/customer/{id}', tags=["Customers"])
def delete_customer(id: int):
    try:
        result = conexion.execute(customers.delete().where(customers.c.id == id))
        conexion.commit()
        if(result.rowcount == 0):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id {id} no encontrado")
        return "Cliente con id ", {id}, "eliminado"
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno de servidor")

@user.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
    try:
        result = conexion.execute(movies.delete().where(movies.c.id == id))
        conexion.commit()
        if(result.rowcount == 0):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id {id} no encontrado")
        return "Pelicula con id ", {id}, "eliminada"
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno de servidor")

@user.delete('/movieStatus/{id}', tags=["MovieStatus"])
def delete_movieStatus(id: int):
    try:
        result = conexion.execute(movieStatus.delete().where(movieStatus.c.id == id))
        conexion.commit()
        if(result.rowcount == 0):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id {id} no encontrado")
        return "Estado con id ", {id}, "eliminado"
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno de servidor")

@user.delete('/userMovies/{id}', tags=["UserMovies"])
def delete_userMovie(id: int):
    try:
        result = conexion.execute(userMovies.delete().where(userMovies.c.id == id))
        conexion.commit()
        if(result.rowcount == 0):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con id {id} no encontrado")
        return f"Registo con id {id} eliminado"
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno de servidor")



    
    
    
    
    
    


