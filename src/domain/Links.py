#!/usr/bin/python3
# -*- coding: utf-8 -*-

import collections
from src.domain.Link import Link
import random


class Links:

    def __init__(self):
        # Map of <word: str, link: Link>
        self.links = collections.OrderedDict()
        self.total_occurrences = 0

    def add_word(self, word):
        if word in self.links:
            self.links[word].increase_quantity()
        else:
            link = Link(word)
            self.links[word] = link
        self.increase_total_occurrences()

    def increase_total_occurrences(self):
        self.total_occurrences += 1

    def choose(self):
        random_number = random.randint(1, self.total_occurrences)
        for word, link in self.links.items():
            random_number -= link.quantity
            if random_number <= 0: return word
