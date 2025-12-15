from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
class Attend(BaseModel):
    name: str
    stream: str
    address: Optional[str]=None #makes this field an optional

datas=[{"name":"ram","stream":"bca","address":"kalikanagar"}]

app=FastAPI()
@app.post("/attendence")
def std_detail(today:Attend): 
    # print(f"name: {today.name}, stream:{today.stream}, address:{today.address}")
    #print(today.model_dump())# .dict() can also be used instead of .model_dump() but is cut as older version
    datas.append(today.model_dump())
    print(today.model_dump())
    return "a student attended",datas
