#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle
from pickle import Unpickler

from MarkovChain import MarkovChain
from file_utils import files_names
from file_utils import sentences
from log import Log
import os

LOG = Log()
FILE = "MarkovChain.ser"


def main():
    markov_chain = get_markov_chain()
    for file_name in files_names():
        markov_chain.process_file(file_name, sentences(file_name))
    pickle.dump(markov_chain, open(FILE, "wb"))


def get_markov_chain():
    if os.path.isfile(FILE):
        with open(FILE, 'rb') as pickle_file:
            return pickle.load(pickle_file)
    else:
        return MarkovChain()


if __name__ == '__main__':
    main()
