from datetime import datetime
from typing import List
from fastapi import HTTPException
from model import GuestbookEntry

guestbook_entries: List[GuestbookEntry] = []
entry_counter = 1

def add_entry(author: str, content: str) -> GuestbookEntry:
    global entry_counter
    entry = GuestbookEntry(id=entry_counter, author=author, content=content, timestamp=datetime.now())
    guestbook_entries.append(entry)
    entry_counter += 1
    return entry

def get_entries() -> List[GuestbookEntry]:
    return guestbook_entries

def delete_entry(entry_id: int):
    global guestbook_entries
    original_length = len(guestbook_entries)
    guestbook_entries = [entry for entry in guestbook_entries if entry.id != entry_id]
    if len(guestbook_entries) == original_length:
        raise HTTPException(status_code=404, detail="Entry not found")
