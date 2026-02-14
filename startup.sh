#!/bin/bash 

source venv/bin/activate

export FLASK_APP=run.py

echo "Starting Pressuredle..."
flask run