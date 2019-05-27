#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Link:

    def __init__(self, word):
        self.word = word
        self.quantity = 1

    def increase_quantity(self):
        self.quantity += 1