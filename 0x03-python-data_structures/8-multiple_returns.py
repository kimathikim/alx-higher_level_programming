#!/usr/bin/python3
def multiple_returns(sentence):
    s = sentence
    if len(s) == 0:
        return (len(s), "None")
    return (len(s), s[0])
