from typing import Dict, List, Optional

# Body(...):  Use this when you expect data to be sent in the body of the HTTP request (usually as JSON). This is common for POST, PUT, and PATCH 
# requests where you are sending data to create, update, or modify resources.

# Path(...): Use this when you have values that are part of the URL path itself. These are often used to identify a specific resource. For example, 
# in /users/{user_id}, the user_id would be a path parameter.

# Query(...): Use this when you have values passed in the query parameters of the URL. These are the key-value pairs that come after the ?
#  in a URL (e.g., /items?q=search_term&limit=10). Query parameters are often optional and used for filtering, sorting, or pagination.
from fastapi import APIRouter, Body, Query, Path # Body, Query and Path are classes proved by fast api for fine grained definition and validation of route params


from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

# FastApi uses Pydantic for data validation
# Here we are creating a blog model class that extends the BaseModel from Pydantic

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nd_comments: int
    published: Optional[bool]
    tags: List[str] = [] # can require our model to have complex types
    metadata: Dict[str, str] = {} # example of maps
    image: Optional[Image] # example of use a custom subtype



# This will require a blog type to be passed to us
# All serialization, deserialization and validation will be handled for use behind the scenes
# This endpoint combines body, path and query params
@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"data": blog, "id": id, "version": version}


# The Query object allows us to add some metadata to our parameter
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                    comment_title: str = Query(None, # No default here, Query validates/defines query params
                                            title="Title of a comment", 
                                            description="Description of comment title", 
                                            alias="commentTitle",
                                            deprecated=True),
                    content: str = Body(..., # ellipsis means it is required 
                                        min_length=10, 
                                        max_length=50, 
                                        regex='^[a-z\s]*$'), # can add far mod complex regex here instead of just lower case letters and spaces
                    optional_content: str = Body("hi how are you"), #Body() is used to define request body parameters. Allow for fin grained control and validation
                    v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']), # Allow for an array of string as multiple query params 
                    comment_id: int = Path(gt=5, le=10)
                    ):
    return {"data": blog, "id": id, "comment_title": comment_title, "comment_id": comment_id, "content": content, "version": v}



def required_functionality():
    return {"message": "Learning fast api"}