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

#request Get method url: "/"
@app.get("/value/{val}")
def value(val):
    return {'your value': val }