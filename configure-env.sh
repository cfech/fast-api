#!/bin/bash

echo "Creating env..."
python3 -m venv fast-api-env
source fast-api-env/bin/activate

echo "installing dependencies"
pip3 install fastapi
pip3 install uvicorn
pip3 install sqlalchemy
pip3 install passlib
pip3 install bcrypt

