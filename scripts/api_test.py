#!/usr/bin/env python

import os
import sys

import requests

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

#response = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address=Kuwait+Salwa+13122")

response = requests.get("https://freemusicarchive.org/api/get/genres.json?api_keyQ7W54CRBAQS4CEPZ")

response_dict = response.json()

for data in response_dict['dataset']:
    print data['genre_title']