from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title: str = "FastApi GET"
app.version: str = "0.0.1"

my_list_users = [
    {
        "id": 1,
        "name": "Leandro",
        "lastname": "Benitez",
        "age": 19,
        "gender": "male",
        "adress": {
            "street": "Av. 1234",
            "number": 1234,
            "city": "CABA",
            "country": "Argentina"
        }
    },
    {
        "id": 2,
        "name": "Juana",
        "lastname": "Benitez",
        "age": 48,
        "gender": "female",
        "adress": {
            "street": "Av. 1234",
            "number": 1234,
            "city": "CABA",
            "country": "Argentina"
        }
    },
    {
        "id": 3,
        "name": "Isa",
        "lastname": "Benitez",
        "age": 1,
        "gender": "female",
        "adress": {
            "street": "Av. 1234",
            "number": 1234,
            "city": "CABA",
            "country": "Argentina"
        }
    },
    {
        "id": 4,
        "name": "Jose",
        "lastname": "Benitez",
        "age": 59,
        "gender": "male",
        "adress": {
            "street": "Av. 1234",
            "number": 1234,
            "city": "CABA",
            "country": "Argentina"
        }
    }
]


@app.get('/', tags=['Home'])
async def init():
    return HTMLResponse('<h1>Hola Bienvenido</h1>')


@app.get('/users', tags=['Users'])
async def users():
    return my_list_users


@app.get('/user/{id}', tags=['Users'])
async def user(id: int):
    for user in my_list_users:
        if user["id"] == id:
            return user
    return HTTPException(404, "User not found")


@app.get('/users/', tags=['Users'])
async def filter_category(over_18: bool, gender: str):
    list_users = []
    for user in my_list_users:
        if user["gender"] == gender:
            if user["age"] >= 18 and over_18 is True:
                list_users.append(user)
            elif user["age"] <= 18 and over_18 is False:
                list_users.append(user)
    return list_users
