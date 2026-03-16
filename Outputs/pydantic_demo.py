from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    CGPA: float = Field(gt=0, lt=10, default=5,description='Thecgps of the student')

new_student = {'name': 'Pranjal', 'age': 21, 'email': "abc@gmial.com", 'CGPA': 9}

student = Student(**new_student)

print(student)
print(type(student))
