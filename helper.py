'''
helper module contains useful function called by gen alg modules
'''

import random
#returns yes or no depending on given probablity
def yes_no(prob):
    if random.random() <= prob:
        return True
    return false
