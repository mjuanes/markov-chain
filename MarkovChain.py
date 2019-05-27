#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.domain.Links import Links


class MarkovChain:

    def __init__(self):

        #Files used to create the chain. Used to not repeat them.
        self.files_names = []
        self.bigrams = {}

    def add_bigram(self, data):
        """
        :param data: words to make the key and the word
        :return:
        """
        key = self.get_key(data)
        word = self.get_word(data)
        links = self.get_bigram_data(key, Links())
        links.add_word(word)
        self.bigrams[key] = links


    def choose_word(self, n_gram):
        """
        :param n_gram: n-tuple of words
        :return: a word
        """
        links = self.bigrams[n_gram]
        return links.choose()

    def get_key(self, data):
        return (data[0], data[1])

    def get_word(self, data):
        return data[2]

    def get_bigram_data(self, bigram, default=None):
        if bigram in self.bigrams:
            return self.bigrams[bigram]
        else:
            return default
