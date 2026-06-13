from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

person =Person(name="Alice", age="30", email="Alice123@gmail.com")
print(person)
