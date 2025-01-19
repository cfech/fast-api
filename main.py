from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response

# import my blog_get obj from the external router
from routers import blog_get
from routers import blog_post

app = FastAPI()

# use the blog get router with this app
app.include_router(blog_post.router)
app.include_router(blog_get.router)

@app.get("/")
def index():
    return "Hello world"


