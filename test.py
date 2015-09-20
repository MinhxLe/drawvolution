#!/bin/python
#import pdb;
#pdb.set_trace()
from circle_org import circle_org
from circ_org_handler import circ_org_handler
#from gen_alg_handler import gen_alg_handler


def main():
    c = circle_org()
    c = circ_org_handler()
    c.simulate_evolution(20,100)
if __name__ == '__main__':
    main()
