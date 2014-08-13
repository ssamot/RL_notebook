#!/bin/bash
python generate_slides.py
echo http://127.0.0.1:8000/RL.slides.html
python -m SimpleHTTPServer 8000

#python -m webbrowser -t "http://127.0.0.1:8000/RL.slides.html"