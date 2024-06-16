from pydantic import BaseModel
from datetime import date

class MarathonBase(BaseModel):
    name: str
    date: date
    region: str
    address: str
    event: str
    homepage: str


class MarathonCreate(MarathonBase):
    pass

class Marathon(MarathonBase):
    id: int

    class Config:
        orm_mode = True
