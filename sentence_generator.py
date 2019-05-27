#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle

from MarkovChain import MarkovChain
from config import CONFIG
from file_utils import files
from file_utils import sentences
from file_utils import text_to_words
from log import Log

LOG = Log()

def main():
    chain = pickle.load(open("MarkovChain.class", "rb"))

    new_review = []
    word1 = "THE"
    word2 = "BEGINNING"

    while True:
        word1, word2 = word2, chain.choose_word((word1, word2))
        if word2 == "END":
            break
        new_review.append(word2)

    print(' '.join(new_review))


if __name__ == '__main__':
    main()
