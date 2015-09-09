

class gen_alg_handler:
    def __init__(init_pop):
        self.MUT_RATE #mutation rate
        #self.DEATH_RATE #
        self.CROSS_RATE #breeding rate


        # stores population in such a manner where we can get population with
        # highest fitness score, select parents based on roulette score to
        # populate next

        self.pop_count
        self.population
        
        #generates initial populatation



    #loops ga algorithm
    #a number of generations
    #TODO: implement parallelism (a lot of repeated work)
    def simulate_evolution(pop_count = 100, gen_count = 10000):
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



    def __initiate_population(count = 100):
        return
     
    #generate probability table for selecting parents to generate next
    #generation based on fitness score
    def __generate_prob_table():
        return
    def __crossover(org1, org2):
        
        return
    
    
    def __gen_rand_org(org_type):
        

    def __mutate(org):
        return
    def get_most_fit():
        return

    
