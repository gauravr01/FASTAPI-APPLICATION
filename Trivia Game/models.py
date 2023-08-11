from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    password: str

class Question(BaseModel):
    text: str
    options: List[str]
    correct_option: int

class Quiz(BaseModel):
    title: str
    description: str
    questions: List[Question]
