from fastapi import FastAPI, HTTPException, Request
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models import User, Question, Quiz

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Sample data for quizzes (you can replace this with a database later)
quizzes = []

# Route to serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.notes.notes.find({})
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "title": doc["title"],
#             "desc": doc["desc"],
#             "imp":doc["imp"]
            
#         })
#     return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})




@app.post("/quizzes/", response_model=Quiz)
def create_quiz(quiz: Quiz):
    """Create a new quiz"""
    quizzes.append(quiz)
    return quiz

@app.get("/quizzes/", response_model=List[Quiz])
def get_quizzes():
    """Get a list of all quizzes"""
    return quizzes

@app.get("/quizzes/{quiz_id}", response_model=Quiz)
def get_quiz(quiz_id: int):
    """Get a specific quiz by ID"""
    if quiz_id < 0 or quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quizzes[quiz_id]

@app.post("/quizzes/{quiz_id}/submit/", response_model=int)
def submit_quiz(quiz_id: int, answers: List[int]):
    """Submit answers for a quiz and calculate the score"""
    if quiz_id < 0 or quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    quiz = quizzes[quiz_id]
    if len(answers) != len(quiz.questions):
        raise HTTPException(status_code=400, detail="Invalid number of answers")
    
    score = 0
    for i, question in enumerate(quiz.questions):
        if 0 <= answers[i] < len(question.options) and answers[i] == question.correct_option:
            score += 1
    
    return score
