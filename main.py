from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


#instance
app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {'data': f'{limit} published blogs form the databse'}
    else:
        return {'data': f'{limit} blogs form the databse'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blod'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2','3'}}

class Blog(BaseModel):
    title :str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f"blog is created with title as {request.title}"}


