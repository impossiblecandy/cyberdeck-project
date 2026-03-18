from fastapi import FastAPI
import random

app = FastAPI()

notes = []

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/notes")
def create_note(note: dict):
    note["id"] = random.randint(1, 10000)
    notes.append(note)
    return note

@app.get("/notes")
def get_notes():
    return notes

