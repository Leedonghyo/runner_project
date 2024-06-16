from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Marathon(Base):
    # 컬럼: 대회명, 대회날짜, 대회지역, 대회 장소, 개최 종목, 홈페이지
    __tablename__ = "marathons"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    date = Column(Date)
    overview = Column(String(255))
    route = Column(String(255))
