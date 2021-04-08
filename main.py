from fastapi import FastAPI

#instance
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'ravi'}}

@app.get('/about')
def about():
    return {'data':'about page'}