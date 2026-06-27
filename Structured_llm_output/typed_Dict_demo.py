from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str


person_typed: Person = {
    "name": "John Doe",
    "age": 30,
    "email": "abc@gmail.com"
}


print(person_typed)