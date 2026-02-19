from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String)
    api_key=Column(String)
    username=Column(String)
class address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    address=Column(String)
    city=Column(String)
    state=Column(String)
    zip_code=Column(String)
class order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    order_date=Column(DateTime,default=datetime.now())
    total_amount=Column(Integer)
    status=Column(String)
   