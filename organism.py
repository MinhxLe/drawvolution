
#from abc import ABCMeta
import random
from bitstring import BitArray



class organism (): 
    #__metaclass__ = abc.ABCMeta #defining a abstract base class
    
    #static vars belonging to the class iself
    DNA_length = 10# representing the length 

    def __init__(self, DNA = BitArray(random.randint(0,2**DNA_length - 1))):
        
        self.DNA = dna
        self.fit_score 
        #@abc.abstractmethod
    def __interpret_DNA__(self):
        return
    
    #@abc.abstractmethod
    def __calc_fitness_score__(self):
        return

class 
