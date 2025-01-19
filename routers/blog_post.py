from typing import Optional
from fastapi import APIRouter, Response
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

# FastApi uses Pydantic for data validation
# Here we are creating a blog model class that extends the BaseModel from Pydantic


class BlogModel(BaseModel):
    title: str
    content: str
    nd_comments: int
    published: Optional[bool]


# This will require a blog type to be passed to us
# All serialization, deserialization and validation will be handled for use behind the scenes
# This endpoint combines body, path and query params
@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"data": blog, "id": id, "version": version}
