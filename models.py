from sqlalchemy import Column, Integer, String

from .database import Base


class Not(Base):
    __tablename__ = "notlar"
    id = Column(Integer, primary_key=True, index=True)
    baslik = Column(String)
    icerik = Column(String)
