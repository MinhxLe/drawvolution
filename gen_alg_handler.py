import random
from bitstring import BitArray
from circle_org import cirle_org

class gen_alg_handler:
    _MUTE_RATE = .001
    _CROSS_RATE = .7
    def __init__(self, pt):
        # stores population in such a manner where we can get population with
        # highest fitness score, select parents based on roulette score to
        # populate next
        self.pop_type = pt
        self.population = set('')

    #loops ga algorithm
    #a number of generations
    #TODO: implement parallelism (a lot of repeated work)
    def simulate_evolution(self, pop_count, gen_count = 150000):
        #initializes population
        tot_fitness = 0 #total fitness of generation
        
        most_fit_org = self.pop_type()
        self.population.add(most_fit_org)
        tot_fitness += most_fit_org.fit_score

        for c in range(pop_count - 1):
            new_org = self.pop_type()
            self.population.add(self.pop_type())
            if new_org.fit_score > most_fit_org.fit_score:
                most_fit_org = new_org

#calculates fitness of generation
#selects parents based on probability ratio of fitness of current gen
#creates 2 new indiv by cerossover
#apply mutaiton to new indiv
#end status check
#repeat
     
    #generate probability table for sele1cting parens to generate next
    #generation based on fitness score
    def __generate_prob_table__(self):
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
            if yes_no(gen_alg_handler._MUT_RATE):
                g != g

    def get_most_fit():
        return
