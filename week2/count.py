#!/usr/bin/env python2

# Python Morsels - Week 2 - Count Words
import re;

re_alphanum = re.compile("[\w']+")


def count_words(sentence):
    words = dict()

    for word in sentence.split():
        try:
            word = re_alphanum.findall(word.lower())[0]
            words[word.lower()] += 1
        except KeyError:
            words[word.lower()] = 1

    return words


if __name__ == "__main__":
    print count_words("oh what a day what a lovely day")
