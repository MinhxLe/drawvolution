
from abc import ABCMeta

from bitstring import BitArray

class organism (object): 
    __metaclass__ = abc.ABCMeta #defining a abstract base class
    
    #static vars belonging to the class iself
    DNA_length

    def __init__(self):
        self.DNA
        #child class will implement whatever data necessary to represent child
        self.fitness_score

    @abc.abstractmethod
    def _interpret_DNA():
        return
    
    @abc.abstractmethod
    def _calc_fitness_score():
        return

    #TODO: method to sort organisms by fitness score
    


