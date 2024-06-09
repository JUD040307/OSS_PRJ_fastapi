from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import List
from model import GuestbookEntry
import guestbook

app = FastAPI()

# Serve static files (HTML, CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/guestbook/", response_model=GuestbookEntry)
def create_entry(author: str, content: str):
    return guestbook.add_entry(author, content)

@app.get("/guestbook/", response_model=List[GuestbookEntry])
def read_entries():
    return guestbook.get_entries()

@app.delete("/guestbook/{entry_id}")
def delete_entry(entry_id: int):
    try:
        guestbook.delete_entry(entry_id)
        return {"message": "Entry deleted successfully"}
    except HTTPException as e:
        raise e