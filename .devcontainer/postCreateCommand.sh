#!/bin/bash

# Define the path to the virtual environment
venv_path=".venv"

# Remove existing .venv folder if it exists
if [ -d "$venv_path" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$venv_path"
fi

# Create a new virtual environment
echo "Creating virtual environment..."
python -m venv "$venv_path"

# Activate the virtual environment
echo "Activating virtual environment..."
source "$venv_path/bin/activate"

# Install packages from requirements.txt
echo "Installing packages from requirements.txt..."
pip install -r requirements.txt

pip install -e .

echo "Virtual environment is set up and activated."
