# fast-api


## Setup 
- `python3 -m venv fast-api-env ` - creates virtual env
- `source fast-api-env/bin/activate` - activates the environment
- `pip3 install fastapi`
- `pip3 install uvicorn ` 

## Running the app 
- `uvicorn main:app --reload`

## VENV
- creates an environment to manage all dependencies
- must source the env in a terminal
- can check by running `which python` and make sure it is using the one from the env


### Uvicorn and Fast API

- Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation, and it plays a crucial role when used with FastAPI. Here's how they work together:   
- FastApi Handles the "logic" of your API: FastAPI provides the tools to define API endpoints, handle requests, validate data, and generate responses. It focuses on the high-level aspects of building APIs, like defining routes and data models.   
- Uvicorn - Serves your FastAPI application: It acts as the web server that runs your FastAPI application, making it accessible to users. Uvicorn handles the low-level details of network communication, receiving incoming requests and sending back responses.   
Enables asynchronous performance: Uvicorn is designed to take full advantage of FastAPI's asynchronous capabilities. It uses an event loop (provided by uvloop and httptools) to efficiently handle multiple requests concurrently, leading to high performance and responsiveness.


## Fast API  Features
- automatic documentation found at `/docs`
  - generate swagger and redoc at `/redoc`
- uses standard python3
- security and authentication are integrated 
- supports dependency injection
- supports validation
- can achieve 100% code coverage 

## Routes
- separate operations into multiple files
- share prefix btw multiple operations
- share tags

## Dependencies
 - allow a function to depend on another function
 - Uses the `Depends()` class