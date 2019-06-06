#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json

CONFIG = None

with open('config.json', 'r') as f:
    CONFIG = json.load(f)


PRECEDENCE_QTY = CONFIG['DEFAULT']['PRECEDENCE_QTY']