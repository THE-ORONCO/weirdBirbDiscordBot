#!/usr/bin/env bash
echo "creating virtual environment..."
python3 -m venv ./.venv

echo "activating virtual environment..."
source "./.venv/bin/activate"

# TODO differentiate between development and deployment by installing stuff like pylint only in dev environments
echo "installing needed packages..."
pip3 install -r requirements.txt

echo "starting setup script..."
python3 ./setup.py

