from typing import Annotated

from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi import FastAPI,Depends

app = FastAPI()
url = "sqlite:///./data_db.db"
engine = create_engine(url, connect_args={'check_same_thread': False})
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

class Table(Base):
    __tablename__ = "Software_Courses"

    Course_id = Column(Integer, primary_key=True, nullable=False)
    Course_name=Column(String)
    Price = Column(String)
    Courses_taken_by = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

class Object(BaseModel):
    Course_id :int
    Course_name: str
    Price :str
    Courses_taken_by : str


@app.post("/post")
def fun(db: Annotated[Session, Depends(get_db)], ob: Object):
    obj = Table(Course_id=ob.Course_id, Course_name=ob.Course_name, Price=ob.Price,Courses_taken_by=ob.Courses_taken_by)
    db.add(obj)
    db.commit()


@app.get("/database/")
def getting_db(db: Annotated[Session, Depends(get_db)]):
    return db.query(Table).all()