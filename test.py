#!/bin/python
from circle_org import circle_org
from circ_org_handler import circ_org_handler
#from gen_alg_handler import gen_alg_handler


def main():
    c = circle_org()
    c = circ_org_handler()
    c.simulate_evolution(10,3)
if __name__ == '__main__':
    main()
