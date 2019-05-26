#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json

config = None

with open('config.json', 'r') as f:
    config = json.load(f)