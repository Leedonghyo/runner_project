from sqlalchemy import Column, Integer, String, Date, UniqueConstraint
from .database import Base


class Marathon(Base):
    # 컬럼: 대회명, 대회날짜, 대회지역, 대회 장소, 개최 종목, 홈페이지
    __tablename__ = "MARATON_SCHEDULE"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    region = Column(String(255))
    address = Column(String(255))
    event = Column(String(255))
    homepage = Column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint('name', 'date', 'homepage', name='_name_date_homepage_uc'),)

