from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

import uvicorn


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/marathons_schedule", response_class=HTMLResponse)
def show_marathons_schedule(request: Request):
    return templates.TemplateResponse("marathons_schedule.html",
                                      {"request": request})


@app.get("/marathons/", response_model=list[schemas.Marathon])
def read_marathons(skip: int = 0, limit: int = 10,
                   db: Session = Depends(get_db)):
    marathons = crud.get_marathons(db, skip=skip, limit=limit)
    return marathons


@app.post("/marathons/", response_model=schemas.Marathon)
def create_marathon(marathon: schemas.MarathonCreate,
                    db: Session = Depends(get_db)):
    return crud.create_marathon(db=db, marathon=marathon)


@app.get("/marathons/{marathon_id}", response_model=schemas.Marathon)
def read_marathon(marathon_id: int, db: Session = Depends(get_db)):
    marathon = crud.get_marathon(db, marathon_id=marathon_id)
    if marathon is None:
        raise HTTPException(status_code=404, detail="Marathon not found")
    return marathon


@app.get("/calendar_events/", response_model=List[dict])
def get_calendar_events(db: Session = Depends(get_db)):
    marathons = crud.get_marathons(db)
    events = [
        {
            "title": marathon.name,
            "start": marathon.date.isoformat(),
            "url": marathon.homepage
        }
        for marathon in marathons
    ]
    return events


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
