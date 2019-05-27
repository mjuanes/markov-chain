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
    markov_chain = get_markov_chain()
    for file in files():
        i = 0
        for sentence in sentences(file):
            custom_sentence = ["THE", "BEGINNING"] + text_to_words(sentence) + ["END"]
            for trigram in generate_trigram(custom_sentence):
                i +=1
                LOG.info("Trigram {}: {}".format(i, str(trigram)))
                markov_chain.add_bigram(trigram)
    pickle.dump(markov_chain, open("MarkovChain.class", "wb"))



def generate_trigram(words):
    if len(words) < 3:
        return
    for i in range(0, len(words) - 2):
        yield (words[i], words[i + 1], words[i + 2])


def beginning():
    CONFIG["PRECEDENCE_QTY"]


def get_markov_chain():
    return MarkovChain()


if __name__ == '__main__':
    main()
