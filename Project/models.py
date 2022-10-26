from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *

Database_url = "postgresql://pavan:Pavan1997@database-1.cj4jm1b9clx6.ap-northeast-1.rds.amazonaws.com:5432/userdetails"
engine = create_engine(Database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(Text)

User.__table__.create(bind=engine, checkfirst=True)

