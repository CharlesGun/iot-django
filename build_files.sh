# !/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run other build commands
python manage.py collectstatic

# Deactivate the virtual environment
deactivate