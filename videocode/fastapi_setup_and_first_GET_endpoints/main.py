from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message":"hello world i am here"}

@app.get('/firstendpoint')
def first_endpoint():
    return {"message":"first endpoint"}