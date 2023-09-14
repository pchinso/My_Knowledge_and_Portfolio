#!/bin/sh
# https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt

echo "Listing your pipenv dependencies:" 
pipenv graph

echo "Creating requirements.txt file" 
pip freeze > requirements.txt

echo "... Finished" 
