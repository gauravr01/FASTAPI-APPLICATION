from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient 

app = FastAPI()

conn = MongoClient("mongodb+srv://gaurav:CzYxQOpnTlj9Nc5u@cluster0.nosubgc.mongodb.net")

# @app.get("/")
# def read_root():
#     return {"Hello": "Gaurav"}




# YZWMl23GPgcmfk9x
#CzYxQOpnTlj9Nc5u
#mongodb+srv://gaurav:<password>@cluster0.nosubgc.mongodb.net/
#mongodb+srv://gaurav:<password>@cluster0.nosubgc.mongodb.net/