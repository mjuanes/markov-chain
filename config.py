#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json

CONFIG = None

with open('config.json', 'r') as f:
    config = json.load(f)