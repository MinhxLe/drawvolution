#!/bin/python
from gen_alg_handler import gen_alg_handler
from circle_org import circle_org

def main():
    c = circle_org()
    g = gen_alg_handler(circle_org)
    g.simulate_evolution(10,10)
    
if __name__ == '__main__':
    main()
