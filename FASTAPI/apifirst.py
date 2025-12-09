from fastapi import FastAPI
app=FastAPI()
@app.get("/about")
def show():
    return "hello";
