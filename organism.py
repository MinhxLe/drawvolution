
from abc import ABCMeta
import random
from bitstring import BitArray



class organism (object): 
    __metaclass__ = abc.ABCMeta #defining a abstract base class
    
    #static vars belonging to the class iself
    DNA_length # representing the length 

    def __init__(self, dna = BitArray(random.randint(0,2**DNA_length - 1))):
        self.DNA = dna
        self.fit_score 


    @abc.abstractmethod
    def __interpret_DNA(self):
        return
    
    @abc.abstractmethod
    def __calc_fitness_score__(self):
        return
    #most fit method gets called by the most fit
    #not necessary but if you want to save an image
    #then we can for the most fit
    @abc.abstractmethod
    def most_fit_method(self):
        return


    #TODO: method to sort organisms by fitness score
    


