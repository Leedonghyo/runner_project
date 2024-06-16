from pydantic import BaseModel
from datetime import date

class MarathonBase(BaseModel):
    name: str
    date: date
    overview: str
    route: str

class MarathonCreate(MarathonBase):
    pass

class Marathon(MarathonBase):
    id: int

    class Config:
        orm_mode = True
