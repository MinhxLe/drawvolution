#!/bin/python

from circle_org import circle_org

def main():
    for x in range (0,11):
        c = circle_org()
        c.save_image("test/test" + str(x) + ".jpg")
if __name__ == '__main__':
    main()
