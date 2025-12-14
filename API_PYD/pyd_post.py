from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body
app=FastAPI()

@app.get("/blog")
def blog():
    return {"this is from get"}

@app.post("/createpost")
def post(payload: dict = Body(...)):
    return {"new_post":f"title {payload['title']} content:{payload['content']}"}


#title str, content str
class Post(BaseModel):
    title: str
    content: str

@app.post("/posting")
def create_post(p: Post):
    print(p)
    return {'data':'new_post'}

class Desc(BaseModel):
    name:str
    roll:int
    add:str

@app.post("/student")
def stu(std:Desc):
    i=0
    print(f"student name ={std.name}, Roll no.={std.roll}, Address={std.add}")
    return {f"created student {i+1}"}

