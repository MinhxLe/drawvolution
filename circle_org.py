from bitstring import BitArray
from PIL import Image, ImageDraw
import random

BYTE_SIZE = 8

class circle_org:
    _CIRC_COUNT = 100
    _CIRC_BIT_COUNT = 10 + 10 + 8 + 8 * 4 #RGBA + position and radius
    DNA_LENGTH = _CIRC_COUNT * _CIRC_BIT_COUNT#overrides this value
    _ref_image = Image.open("dickbutt.jpg")
    #circle image drawing
    def __init__(self, dna):
        self.DNA = dna
        self.image = Image.new('RGB', circle_org._ref_image.size, "black")
        self.img_editor = ImageDraw.Draw(self.image, 'RGBA')
        self.__interpret_DNA__()
        self.__calc_fitness_score__()

    def __init__(self):
        self.DNA = dna = BitArray(bin(random.randint(0,2**self.DNA_LENGTH -
            1)))
        self.image = Image.new('RGB', circle_org._ref_image.size, "black")
        self.img_editor = ImageDraw.Draw(self.image, 'RGBA')
        self.__interpret_DNA__()
        self.__calc_fitness_score__()

    def save_image(self, name):
        self.image.save(name)
    
    @staticmethod
    def set_ref_image(img_name):
        circle_org.ref_image = Image.open(img_name)


    def __calc_fitness_score__(self):
        return

    def __interpret_DNA__(self):
        #c represent sthe shift
        for c in range(0, circle_org._CIRC_COUNT):
            shift = circle_org._CIRC_BIT_COUNT * c
            x = self.DNA[shift:shift+10].uint
            shift += 10
            y = self.DNA[shift:shift+10].uint
            shift += 10
            r = self.DNA[shift:shift+BYTE_SIZE].uint
            shift += BYTE_SIZE
            R = self.DNA[shift:shift+BYTE_SIZE].uint
            shift += BYTE_SIZE
            G = self.DNA[shift:shift+BYTE_SIZE].uint
            shift += BYTE_SIZE
            B = self.DNA[shift:shift+BYTE_SIZE].uint
            shift += BYTE_SIZE
            A = self.DNA[shift:shift+BYTE_SIZE].uint
            shift += BYTE_SIZE
            self.img_editor.ellipse([(x - r, y - r), (x+r, y+r)], (R,G,B,A),
                    (R,G,B,A))

