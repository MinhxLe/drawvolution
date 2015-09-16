'''
helper module contains useful function called by gen alg modules
'''

from random import random

#returns yes or no depending on given probablity
def yes_no(prob):
    if random() <= prob:
        return True
    return False

#SOURCE: http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python
def weighted_choice(choices, weights):
    rnd = random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return choices[i]
