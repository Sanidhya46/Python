# basically this file is used for making migrations of your database

#! /bin/bash

sleep 10  # pause execution for 10 seconds
python3 manage.py makemigrations
python3 manage.py migrate