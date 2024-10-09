# API CRUD para Gestión de Películas y Clientes

Esta API está diseñada para gestionar una base de datos de clientes y películas utilizando FastAPI y SQLAlchemy. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los recursos de clientes, películas, estados de películas y asociaciones de usuarios con películas.

## Características

- **Clientes**: Gestión de información de clientes.
- **Películas**: Gestión de información sobre películas.
- **Estados de Películas**: Seguimiento de los estados de las películas.
- **Usuarios y Películas**: Asociación entre usuarios y las películas que están viendo.
- **Validaciones**: Validaciones integradas para los datos de entrada utilizando Pydantic.

## Validaciones

- **Email**: Se valida que el formato del email sea correcto.
- **Contraseña**: Se exige que la contraseña cumpla con los siguientes requisitos:
  - Longitud mínima de 8 caracteres.
  - Al menos una letra mayúscula.
  - Al menos un número.
  - Al menos un carácter especial.
  - Al menos un carácter no alfabético.
- **Teléfono**: El número de teléfono debe tener exactamente 9 dígitos y comenzar con 6 o 7.
- **Año de la película**: El año debe ser un valor válido entre 1900 y el año actual.

## Tecnologías Usadas

- **FastAPI**: Framework web para construir APIs.
- **SQLAlchemy**: ORM para interactuar con bases de datos.
- **Cryptography**: Para el manejo seguro de contraseñas.
- **Pydantic**: Para la validación de datos.
- **Password Strength**: Para validar la fortaleza de contraseñas.
- **Validate Email**: Para validar la estructura de los correos electrónicos.

## Rutas de la API

### Clientes (`/customer`)

- **GET** `/customer`: Obtiene todos los clientes.
- **POST** `/customer`: Crea un nuevo cliente.
- **PUT** `/customer`: Actualiza un cliente existente (requiere ID).
- **DELETE** `/customer/{id}`: Elimina un cliente por ID.

### Películas (`/movies`)

- **GET** `/movies`: Obtiene todas las películas.
- **POST** `/movies`: Crea una nueva película.
- **PUT** `/movies`: Actualiza una película existente (requiere ID).
- **DELETE** `/movies/{id}`: Elimina una película por ID.

### Estados de Películas (`/movieStatus`)

- **GET** `/movieStatus`: Obtiene todos los estados de películas.
- **POST** `/movieStatus`: Crea un nuevo estado de película.
- **PUT** `/movieStatus`: Actualiza un estado de película existente (requiere ID).
- **DELETE** `/movieStatus/{id}`: Elimina un estado de película por ID.

### Asociaciones de Usuarios y Películas (`/userMovies`)

- **GET** `/userMovies`: Obtiene todas las asociaciones de usuarios y películas.
- **POST** `/userMovies`: Crea una nueva asociación.
- **PUT** `/userMovies`: Actualiza una asociación existente (requiere ID).
- **DELETE** `/userMovies/{id}`: Elimina una asociación por ID.

## Ejecución del Proyecto

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/AlejandroJimenez16/CRUD_FastAPI_UsuPelis.git

2. Navega al directorio del proyecto:
   ```bash
   cd CRUD_FastAPI_UsuPelis
   
3. Asegúrate de tener Python y las dependencias necesarias instaladas.
4. Ejecuta el siguiente comando para iniciar el servidor:
   ```bash
   uvicorn app:app --reload

## Acceso a Swagger

Swagger UI está disponible para facilitar la interacción con la API y para la documentación automática de las rutas. Puedes acceder a Swagger en la siguiente URL:

`http://localhost:8000/docs`

![image](https://github.com/user-attachments/assets/0ffc056e-a7d1-406f-a6ee-55120d4cde97)


