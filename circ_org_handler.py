import random
from bitstring import BitArray
from circle_org import circle_org
from helper import yes_no, weighted_choice

class circ_org_handler:
    MUT_RATE = .005
   # CROSS_RATE = .7
    
    def simulate_evolution(self, pop_count = 100, gen_count = 150000,
            save_folder = 'test/'):
        #initializes population
        tot_fitness = 0 #total fitness of generation
        population = []
        pop_weight = []
        most_fit_org = circle_org()
        population.append(most_fit_org)
        pop_weight.append(most_fit_org.fit_score)
        tot_fitness += most_fit_org.fit_score

        for c in range(pop_count - 1):
            new_org = circle_org()
            population.append(new_org)
            pop_weight.append(new_org.fit_score)
            tot_fitness += new_org.fit_score
            if new_org.fit_score > most_fit_org.fit_score:
                most_fit_org = new_org

        #begins loop for evolution
        cond = True #TODO: stop loop if certain fitscore is met
        for x in range(0, gen_count):
            #saving most fit
            if x % 20 == 0:
                most_fit_org.save_image('test/' + str(x) + ".png")
            #print (most_fit_org.fit_score)
            most_fit_org.fit_score = 0 #TODO: DIRTY, FIX THIS

            temp_population  = []#temporary population buff
            new_pop_count = 0
            while new_pop_count < pop_count:
                #2 new individuals
                p1 = weighted_choice(population, pop_weight)
                p2 = weighted_choice(population, pop_weight)
                #if yes_no(circ_org_handler.CROSS_RATE):
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
        return (circle_org(new_org_dna[0], False),
                circle_org(new_org_dna[1], False))


    #DNA BITSTRING PRIVATE METHODS
    def __crossover__(self, dna1, dna2):
        start = random.randint(0, circle_org.DNA_LENGTH - 1)
        return ((dna1[0:start] + dna2[start:]),
            (dna2[0:start] + dna1[start:]))

        '''
        start = random.randint(circle_org.DNA_LENGTH)
        #decides which dna string 
        if random.choice([0,1]):
            return org_type(org1.DNA[0:start] + org2.DNA[start:])
        else:
            return org_type(org2.DNA[0:start] + org1.DNA[start:])

        '''
    def __mutate__(self,dna):
        num_bit_flip = int(circ_org_handler.MUT_RATE * dna.length)
        for x in range(0, num_bit_flip):
            bit_to_flip = random.randint(0, dna.length - 1)
            if dna[bit_to_flip]:
                dna[bit_to_flip] = 0
            else:
                dna[bit_to_flip] = 1

