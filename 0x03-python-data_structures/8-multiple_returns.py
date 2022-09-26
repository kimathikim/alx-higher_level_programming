#!/usr/bin/python3
def multiple_returns(sentence):
    s = sentence
    t = ()
    if s != 0:
        t += len(s),
        t += s[0],
        return (t)
    t += len(s),
    t += None,
    return (t)
