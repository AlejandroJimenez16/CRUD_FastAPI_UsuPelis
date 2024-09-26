from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from password_strength import PasswordPolicy
from validate_email import validate_email

class Customer(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[int] = None
    create_at: Optional[datetime] = None
    update_date: Optional[datetime] = None
    
    #Validacion email
    @field_validator('email')
    def validate_email(cls, e):
        valido = validate_email(e)
        
        if not valido:
            raise ValueError("El email introducido no es correcto")
        return e    
        
    #Validación password
    @field_validator('password')
    def validate_password(cls, p):
        policy = PasswordPolicy.from_names(
            length = 8,
            uppercase = 1,
            numbers = 1,
            special = 1,
            nonletters = 1
        )
        
        validacion = policy.test(p)
        
        if validacion:
            raise ValueError('La contraseña no cumple con los requisitos mínimos de seguridad')
        return p

    # Validación phone
    @field_validator('phone')
    def validate_phone(cls, p):
        p = str(p)
        if len(p) != 9 or (p[0] not in ['6', '7']):
            raise ValueError('El número de teléfono debe tener exactamente 9 dígitos y empezar por 6 o 7')
        return p
    
    
class Movie(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    create_at: Optional[datetime] = None
    update_date: Optional[datetime] = None
    
    # Validación year
    @field_validator('year')
    def validate_movie_year(cls, y):
        current_year = datetime.now().year
        if(y <1900 or y > current_year):
            raise ValueError('El año introducido no es válido, solo es válido del 1900 al actual')
        return y
        
class MovieStatus(BaseModel):
    id: Optional[int] = None
    status: Optional[str] = None
    create_at: Optional[datetime] = None
    update_date: Optional[datetime] = None
    
class UserMovies(BaseModel):
    id: Optional[int] = None
    idCustomer: Optional[int] = None
    idMovie: Optional[int] = None
    idStatus: Optional[int] = None
    create_at: Optional[datetime] = None
    update_date: Optional[datetime] = None
    
