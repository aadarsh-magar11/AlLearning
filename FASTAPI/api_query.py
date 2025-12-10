from fastapi import FastAPI

app=FastAPI()
@app.get("/number")
def display(value):
    return {"data": f"your data is {value}"}

@app.get("/chatWithGirl")
def chat(name,status):
    if(status.lower()=="single"):
        return {"msg":f"Hello {name}, as you are {status}, I would like to stay in relationship with you"}
    else:
        return {"msg":f"Hello {name}, since you are {status}, why are you cheating your girlfriend"}