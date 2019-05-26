#!/usr/bin/python3
# -*- coding: utf-8 -*-


class MarkovChain:
    """
    Files set used to create the chain
    Used to not repeat.
    """
    files_names = []

    def __init__(self):
        self.files_names = []

    """
    map  key[pair of words] -> map(word -> quantity of occurrences)
    """
    bigrams = {}

    def add_bigram(self, bigram, word):
        """
        :param bigram: par of 2 words (word1, words 2)
        :param word: the third word of the program
        :return:
        """
        bigram_data = self.get_bigram_data(bigram)
        bigram_data = [] if bigram_data is None else bigram_data
        bigram_data[word] = 0 if word not in bigram_data else bigram_data[word] + 1
        self.bigrams[bigram] = bigram_data

    def get_bigram_data(self, bigram):
        if bigram in self.bigrams:
            return self.bigrams[bigram]
        else:
            None
