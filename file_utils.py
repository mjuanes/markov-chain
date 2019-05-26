#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re

WORD_PATTEN = re.compile("[\wáéíóúüÁÉÍÓÚÜ]{1,}", re.IGNORECASE)
FILES_RELATIVE_PATH = "./texts"


def files():
    files = os.listdir(FILES_RELATIVE_PATH)
    for file in files:
        full_path = os.path.abspath(FILES_RELATIVE_PATH + file)
        yield full_path


# Receives a file
def sentences(file):
    line_buffer = ""
    for line in file.readlines():
        line_buffer = line_buffer + " " + sanitize_line(line)
        if line_buffer.endswith("."):
            sentences = line_buffer.split(".")
            for sentence in sentences[0: len(sentences)-1]:
                yield sentence
            line_buffer = ""
        elif "." in line_buffer:
            sentences = line_buffer.split(".")
            for sentence in sentences[0:len(sentences) - 2]:
                yield sentence
            line_buffer = sentences[len(sentences)-2]

def text_to_words(text):
    return WORD_PATTEN.findall(text)


def sanitize_line(line):
    return line.replace('\n', ' ').replace('  ', ' ').strip()
