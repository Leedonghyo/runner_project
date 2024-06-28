from sqlalchemy.orm import Session
from . import models, schemas


def get_marathon(db: Session, marathon_id: int):
    return db.query(models.Marathon).filter(models.Marathon.id == marathon_id).first()


def get_marathons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Marathon).offset(skip).limit(limit).all()


def create_marathon(db: Session, marathon: schemas.MarathonCreate):
    db_marathon = models.Marathon(**marathon.dict())
    db.add(db_marathon)
    db.commit()
    db.refresh(db_marathon)
    return db_marathon
