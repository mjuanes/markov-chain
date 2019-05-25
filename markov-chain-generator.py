#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


def main():
    files = os.listdir("./texts")
    for file in files:
        path = os.path.abspath("./texts/" + file)
        print(path)
        file = open(path, "r")
        for line in read_sentences(file):
            print("Oración:" + line)
        file.close()


def read_sentences(file):
    line_buffer = ""
    for line in file.readlines():
        line_buffer = line_buffer + " " + sanitize_line(line)
        if line_buffer.endswith("."):
            sentences = line_buffer.split(".")
            for sentence in sentences[0: len(sentences)-1]:
                yield sentence
            line_buffer = ""
        elif "." in line_buffer:
            sentences = (line_buffer).split(".")
            for sentence in sentences[0:len(sentences) - 2]:
                yield sentence
            line_buffer = sentences[len(sentences)-2]


def sanitize_line(line):
    return line.replace('\n', ' ').replace('  ', ' ').strip()

if __name__ == '__main__':
    main()
