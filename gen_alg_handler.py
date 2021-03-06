import random
from bitstring import BitArray
from circle_org import circle_org
from helper import yes_no, weighted_choice

class gen_alg_handler:
    MUT_RATE = .005
    #CROSS_RATE = .7
    def __init__(self,pt):
        # stores population in such a manner where we can get population with
        # highest fitness score, select parents based on roulette score to
        # populate next
        self.pop_type = pt
        #self.population = set('')

    #loops ga algorithm
    #a number of generations
    #TODO: implement parallelism (a lot of repeated work)
    def simulate_evolution(self, pop_count = 100, gen_count = 150000,
            save_folder = 'test/'):
        #initializes population
        tot_fitness = 0 #total fitness of generation
        population = []
        pop_weight = []
        most_fit_org = self.pop_type()
        population.append(most_fit_org)
        pop_weight.append(most_fit_org.fit_score)
        tot_fitness += most_fit_org.fit_score

        for c in range(pop_count - 1):
            new_org = self.pop_type()
            population.append(new_org)
            pop_weight.append(new_org.fit_score)
            tot_fitness += new_org.fit_score
            if new_org.fit_score > most_fit_org.fit_score:
                most_fit_org = new_org

        #begins loop for evolution
        cond = True #TODO: stop loop if certain fitscore is met
        for x in range(0, gen_count):
            #saving most fit
            if x % 100 == 0:
                most_fit_org.save_image('test/' + str(x) + ".png")
            #print (most_fit_org.fit_score)
            most_fit_org.fit_score = 0 #TODO: DIRTY, FIX THIS

            temp_population  = []#temporary population buff
            new_pop_count = 0
            while new_pop_count < pop_count:
                #2 new individuals
                p1 = weighted_choice(population, pop_weight)
                p2 = weighted_choice(population, pop_weight)
                #if yes_no(gen_alg_handler.CROSS_RATE):
                    #select 2 parents
                kids = self.gen_new_org(p1,p2)
                for kid in kids:
                    if kid.fit_score > p1.fit_score or kid.fit_score > p2.fit_score:
                        temp_population.append(kid)
                        new_pop_count += 1
                        if kid.fit_score >= most_fit_org.fit_score:
                            most_fit_org = kid
            population = temp_population

#calculates fitness of generation
#selects parents based on probability ratio of fitness of current gen
#creates 2 new indiv by cerossover
#apply mutaiton to new indiv
#end status check
#repeat
    def gen_new_org(self, org1,org2):
        new_org_dna = self.__crossover__(org1.DNA, org2.DNA)
        for dna in new_org_dna:
           self.__mutate__(dna)
        #print (new_org_dna[1].bin)
        return (self.pop_type(new_org_dna[0], False),
                self.pop_type(new_org_dna[1], False))


    #DNA BITSTRING PRIVATE METHODS
    def __crossover__(self, dna1, dna2):
        start = random.randint(0, self.pop_type.DNA_LENGTH)
        return ((dna1[0:start] + dna2[start:]),
            (dna2[0:start] + dna1[start:]))

        '''
        start = random.randint(self.pop_type.DNA_LENGTH)
        #decides which dna string 
        if random.choice([0,1]):
            return org_type(org1.DNA[0:start] + org2.DNA[start:])
        else:
            return org_type(org2.DNA[0:start] + org1.DNA[start:])

        '''
    def __mutate__(self,dna):
        for x in range(0, dna.length):
            if yes_no(gen_alg_handler.MUT_RATE):
                dna[x] = ~dna[x]


