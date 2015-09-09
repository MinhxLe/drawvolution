import random
from bitstring import BitArray
import helper


class gen_alg_handler:
    def __init__(self):
        self.MUT_RATE #mutation rate
        #self.DEATH_RATE #
        self.CROSS_RATE #breeding rate


        # stores population in such a manner where we can get population with
        # highest fitness score, select parents based on roulette score to
        # populate next

        self.pop_count
        self.pop_type
        self.population
        
        #generates initial populatation

    #loops ga algorithm
    #a number of generations
    #TODO: implement parallelism (a lot of repeated work)
    def simulate_evolution(self, pop_count = 100, gen_count = 10000):
        #initializes population
        tot_fitness = 0 #total fitness of generation
        for c in range(pop_count):
            __gen_rand_org(org)


#calculates fitness of generation
#selects parents based on probability ratio of fitness of current gen
#creates 2 new indiv by cerossover
#apply mutaiton to new indiv
#end status check
#repeat



    def __initiate_population(self, count = 100):
         return
     
    #generate probability table for sele1cting parens to generate next
    #generation based on fitness score
    def __generate_prob_table(self):
        return
    
    
    def __crossover__(self, org1, org2):
        start = random.randint(self.pop_type.DNA_length)
        #decides which dna string 
        if random.choice([0,1]):
            return org_type(org1.DNA[0:start] + org2.DNA[start:])
        else:
            return org_type(org2.DNA[0:start] + org1.DNA[start:])


    def __mutate__(self,org):
        for g in org.DNA:
            if yes_no(self.MUT_RATE):
                g != g

    def get_most_fit():
        return
