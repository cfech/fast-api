#!/bin/bash

echo "Creating env..."
python3 -m venv fast-api-env
source fast-api-env/bin/activate

echo "installing dependencies"
pip3 install fastapi
pip3 install uvicorn

