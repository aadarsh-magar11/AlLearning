from fastapi import FastAPI
app=FastAPI()
@app.get("/login")#here @app is a decorator that makes normal function link to api
#and / is used to 
def login():
    return "you have logged in"

@app.get("/users")
def showusers():
    return ["ram","shyam","sita"]

@app.get("/fruits")
def fruits():
    return ["banana","apple"]

@app.get("/value/one")
def next_value():
    return {"data":"this must be above the dynamic path"}

#request Get method url: "/"
@app.get("/value/{int}")
def value(val: int):#this makes the value into integer rather than string
    return {'your value': val}