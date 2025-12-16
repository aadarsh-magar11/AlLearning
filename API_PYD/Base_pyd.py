from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Attend(BaseModel):
    name: str
    id: int
    stream: str
    address: Optional[str] = None

datas = [
    {"name": "ram", "id": 1, "stream": "bca", "address": "kalikanagar"},
    {"name": "ram", "id": 2, "stream": "bca", "address": "kalikanagar"}
]

# ---------------- POST with random ID ----------------
@app.post("/posts")
def create_posts(att: Attend):
    att_dict = att.model_dump()
    datas.append(att_dict)
    return {"data": att_dict}

# ---------------- POST attendance ---------------------------------------------------------------------------------------------
@app.post("/attendence")
def std_detail(today: Attend):
    datas.append(today.model_dump())
    return {"message": "student attended", "data": datas}

# ---------------- helper ----------------------------------------------------------------------------------------------
def find_post(id: int):
    for p in datas:
        if p.get("id") == id:
            return p
        
    #function to return the index of the dictionary
def find_index_post(id):
    for i,p in enumerate(datas): #this returns the index value pair
        if p["id"]==id:
            return i

# ---------------- GET routes --------------------------------------------------------------------------------------------

@app.get("/blog/{id}")
def get_blog_id(id: int, response: Response):
    post = find_post(id)

    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"post with id:{id} was not found"}

    return {"data": post}

#==============DELETING A POST=======================================================================================
@app.delete("/posts/{id}")
def delete_post(id: int, response:Response):
    #deleting post
    #find the index in the array that has the required id
    #datas.pop(index) 
    index=find_index_post(id)
    if index == None:
        response.status_code=status.HTTP_404_NOT_FOUND
        return("couldnot delete the data")
    datas.pop(index)
    return {"message":"successfully"}

@app.get("/total_datas")
def show():
    return datas

#==============Updating post===================================================================================================================
@app.put("/posts/{id}")
def update_post(id:int, post=Attend, response=Response):
    index=find_index_post(id)
    if index == None:
        response.status_code=status.HTTP_404_NOT_FOUND
        return("couldnot delete the data")
    post_dict=post.model_dump()
    post_dict['id']=id
    post_dict[index]=post_dict
    return {"data":post_dict}

