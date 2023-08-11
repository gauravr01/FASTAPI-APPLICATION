from fastapi import APIRouter
from modals.note import Note
from config.db import conn
from schema.note import notesEntity,noteEntity
from fastapi import Request
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse
note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "imp":doc["imp"]
            
        })
    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})

# @note.post("/")
# def add_note(note: Note ):
#     inserted_note = conn.notes.notes.insert_one(dict(note))

#     return noteEntity(inserted_note)

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["imp"] = True if formDict.get("imp") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success":"True"}
