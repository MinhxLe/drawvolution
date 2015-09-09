
from abc import ABCMeta
import random
from bitstring import BitArray

class organism (object): 
    __metaclass__ = abc.ABCMeta #defining a abstract base class
    
    #static vars belonging to the class iself
    DNA_length # representing the length 

    def __init__(self, dna = BitArray(random.randint(0,2**DNA_length - 1))):
            self.DNA = dna

    @abc.abstractmethod
    def ___interpret_DNA__(self):
        return
    
    @abc.abstractmethod
    def __calc_fitness_score__(self):
        return

    #TODO: method to sort organisms by fitness score
    


