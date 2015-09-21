#!/bin/python
from circle_org import circle_org
from circ_org_handler import circ_org_handler
#from gen_alg_handler import gen_alg_handler
#import cProfile

def main():
    #pr = cProfile.Profile()
    #c = circle_org()
    #c.save_image("test.png")
    c = circ_org_handler()
    #pr.enable()
    c.simulate_evolution(50,10)
    #pr.disable()
    #pr.print_stats()
if __name__ == '__main__':
    main()
