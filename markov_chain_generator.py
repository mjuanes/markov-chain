#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from file_utils import files
from file_utils import sentences
from file_utils import text_to_words
from MarkovChain import MarkovChain


def main():
    markov_chain = get_markov_chain()
    for file in files():
        for sentence in sentences(file):
            custom_sentence = ["THE", "BEGINNING"] + sentence + ["END"]
            for trigram in generate_trigram(custom_sentence):
                markov_chain.add_bigram()


def generate_trigram(words):
    if len(words) < 3:
        return
    for i in range(0, len(words) - 2):
        yield (words[i], words[i + 1], words[i + 2])


def get_markov_chain():
    return MarkovChain()


if __name__ == '__main__':
    main()
