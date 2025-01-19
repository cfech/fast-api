from enum import Enum
from typing import Optional
from fastapi import APIRouter, Depends, Response, status

from routers.blog_post import required_functionality # depends ket word allows for linking dependencies 


# can define a router and give every route in this file some standard settings
router = APIRouter(prefix="/blog", tags=["blog"])


# Order of the defined endpoints is important
# @app.get("/blog/all")
# def get_blog():
#     return {'message' : f"All blogs"}


# Example of of query params with default values
# Can use the python optional class for defaults as well
@router.get("/all", 
         summary="Retrieves all blogs", 
         description="This api call simulates fetching all blogs",
         response_description="Available blogs"
         )
def get_all_blogs(page=1, 
                    page_size: Optional[int] = 10,
                    required_param: dict = Depends(required_functionality) # this function will be called by this endpoint because it is required, injecting functionality
                    ):
    return {"message": f"All {page_size} blogs on {page}",  "required_param": required_param}


# Example with query and path params in the same endpoint
# Tags allows us to better organize our endpoints
@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    # Can also define the description in a doc string
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path param
    - **comment_id** mandatory path param
    - **valid** optional query param
    - **username** optional query param
    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


# Predefined values with enum, this endpoint will only accept these types
class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type{type}")
def get_blog(type: BlogType):
    return {'message': f"Blog with type {type}"}


# Example of typed named param
# Fast API will handle the validation for us with Pydantic allow us to type the arguments
# Can pass a status code for the response here
# Cna also pas a response object into the endpoint method
@router.get("/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog with id {id} not found"}

    return {'message': f"Blog with id {id}"}
