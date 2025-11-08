#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt 
exec python3 bot:app --bind 0.0.0.0:$PORT
