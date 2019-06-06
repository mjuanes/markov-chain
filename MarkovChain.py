#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.domain.Links import Links
from file_utils import text_to_words
import config

class MarkovChain:

    def __init__(self):

        # Files used to create the chain. Used to not repeat them.
        self.files_names = []

        # Map from n-gram to Links
        self.bigrams = {}


    def process_file(self, file, sentence_generator):
        if file.name not in self.files_names:
            for sentence in sentence_generator:
                self.process_sentence(sentence)
            self.files_names.append(file.name)

    def process_sentence(self, sentence):
        custom_sentence = ["THE", "BEGINNING"] + text_to_words(sentence) + ["END"]
        for ngram in self.generate_ngram(custom_sentence):
            self.add_bigram(ngram)

    def add_bigram(self, data):
        """
        :param data: words to make the key and the word
        :return:
        """
        key = self.get_key(data)
        word = self.get_word(data)
        links = self.get_bigram_data(key, orElse=Links())
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

    def has_process(self, file):
        return file in self.files_names

    @staticmethod
    def generate_ngram(words):
        if len(words) < config.PRECEDENCE_QTY:
            return
        for i in range(0, len(words) - 2):
            yield (words[i], words[i + 1], words[i + 2])


    def get_bigram_data(self, bigram, orElse=None):
        if bigram in self.bigrams:
            return self.bigrams[bigram]
        else:
            return orElse
