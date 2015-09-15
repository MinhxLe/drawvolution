from bitstring import BitArray
from PIL import Image, ImageDraw
import random

BYTE_SIZE = 8

class circle_org:
    _IMAGE_NAME = 'dickbutt.jpg'
    #solution space limitations
    _CIRC_COUNT = 100
    _IMAGE_MODE = "RGBA" #TODO: change to enum
    
    #solution space dna limitation
    _H_DIM_BIT_COUNT = 10 # size of pictures can be up to 2^10
    _W_DIM_BIT_COUNT = 10
    _R_DIM_BIT_COUNT = 8
    # _MODE_BIT_COUNT #RGB or grey scale

    if _IMAGE_MODE == 'L':
        _MODE_BIT_COUNT = 8 #grey scale, no alpha
        _REF_IMAGE = Image.open(_IMAGE_NAME).convert('L')
    elif _IMAGE_MODE == 'RGBA':
        _MODE_BIT_COUNT = 8 * 4 #RGBA 
        _REF_IMAGE = Image.open(_IMAGE_NAME)
    else:
        #TODO: error handling
        _MODE_BIT_COUNT = -1
        _REF_IMAGE  = Image.open(_IMAGE_NAME)
    
    _CIRC_BIT_COUNT = (_H_DIM_BIT_COUNT * _W_DIM_BIT_COUNT *
        _R_DIM_BIT_COUNT * _MODE_BIT_COUNT) 
    DNA_LENGTH = _CIRC_COUNT * _CIRC_BIT_COUNT

    #solution image information(part of class to prevent multiple computaiton
    _REF_IMAGE_DATA = _REF_IMAGE.getdata()

    #circle image drawing
    def __init__(self, dna):
        self.DNA = dna
        self.image = Image.new('RGB', circle_org._REF_IMAGE.size, "white")
        
        if circle_org._IMAGE_MODE == 'RGBA':
            self.img_editor = ImageDraw.Draw(self.image, 'RGBA')
        elif circle_org._IMAGE_MODE == 'L':
            self.img_editor = ImageDraw.Draw(self.image, 'L')
        
        self.__interpret_DNA__()
        
        self.fit_score = self.__calc_fitness_score__()

    def __init__(self):
        self.DNA = dna = BitArray(bin(random.randint(0,2**self.DNA_LENGTH -
            1)))
        self.image = Image.new('RGB', circle_org._REF_IMAGE.size, "white")
        
        if circle_org._IMAGE_MODE == 'RGBA':
            self.img_editor = ImageDraw.Draw(self.image, 'RGBA')
        elif circle_org._IMAGE_MODE == 'L':
            self.img_editor = ImageDraw.Draw(self.image, 'L')
        
        self.__interpret_DNA__()
        self.fit_score = self.__calc_fitness_score__()

    def save_image(self, name):
        self.image.save(name)
    
    @staticmethod
    def set_ref_image(img_name):
        circle_org._REF_IMAGE = Image.open(img_name)


    def __calc_fitness_score__(self):
        #TODO:naive implementation, compares every pixel 
        
        
        raw_error_acc = 0 
        for new,orig in zip(circle_org._REF_IMAGE_DATA, self.image.getdata()):
            for new_col, orig_col in zip(new, orig):
                raw_error_acc += abs(new_col - orig_col)
                return raw_error_acc 

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
            if circle_org._IMAGE_MODE == 'RGBA':
                R = self.DNA[shift:shift+BYTE_SIZE].uint
                shift += BYTE_SIZE
                G = self.DNA[shift:shift+BYTE_SIZE].uint
                shift += BYTE_SIZE
                B = self.DNA[shift:shift+BYTE_SIZE].uint
                shift += BYTE_SIZE
                A = self.DNA[shift:shift+BYTE_SIZE].uint
                shift += BYTE_SIZE
                color = (R,G,B,A)
            elif circle_org._IMAGE_MODE == 'L':
                L = self.DNA[shift:shift+BYTE_SIZE].uint
                shift += BYTE_SIZE
                color = (L)
            else:
                #TODO ERROR HANDLING!
                return
            self.img_editor.ellipse([(x - r, y - r), (x+r, y+r)], color, color)

