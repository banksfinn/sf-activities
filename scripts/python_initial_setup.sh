#!/bin/bash
echo "Creating initial virtual environment"
python3.10 -m venv venv
echo "Creating activating virtual environment"
source venv/bin/activate
echo "Installing requirements"
pip install -r requirements.txt
echo "Initial setup completed!"
