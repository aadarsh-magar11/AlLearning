from fastapi import FastAPI

app=FastAPI()
@app.post("/posted")
def func():
    print("{'msg':'you posted using api'}")