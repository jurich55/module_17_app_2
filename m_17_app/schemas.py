
from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    titl: str
    content: str
    age: int

class UpdateTask(BaseModel):
    titl: str
    content: str
    age: int
