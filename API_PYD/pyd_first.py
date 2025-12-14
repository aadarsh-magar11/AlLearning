from fastapi import FastAPI

app=FastAPI()
@app.post("/posted")
def func():
    print("{'msg':'you posted using api'}")


@app.post('/blog')
def create(title,body):
    return {'title':title,'body':body}

