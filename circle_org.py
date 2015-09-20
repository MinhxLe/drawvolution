from bitstring import BitArray
from PIL import Image, ImageDraw
import multiprocessing
from multiprocessing import Pool
import imagehash
import random

from operator import itemgetter

BYTE_SIZE = 8

#todo: implement rgba
def calc_rgba(tup):
    return

def calc_l(tup):
    raw_error_acc = 0
    for new,orig in zip(tup[0], tup[1]):
        raw_error_acc += abs(new - orig)
    return raw_error_acc

class circle_org:
    _IMAGE_NAME = 'sad_pepe.png'
    #solution space limitations
    _CIRC_COUNT = 128
    _IMAGE_MODE = "L" #TODO: change to enum
    
    #solution space dna limitation
    X_BIT_COUNT = 8 # size of pictures can be up to 2^10
    Y_BIT_COUNT = 8
    Z_BIT_COUNT = 8
    R_BIT_COUNT = 8
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
    
    _CIRC_BIT_COUNT = (X_BIT_COUNT + Y_BIT_COUNT + 
        Z_BIT_COUNT + R_BIT_COUNT + _MODE_BIT_COUNT) 
    DNA_LENGTH = _CIRC_COUNT * _CIRC_BIT_COUNT

    #solution image information(part of class to prevent multiple computaiton
    _REF_IMAGE_DATA = _REF_IMAGE.getdata()
    REF_IMAGE_HASH = imagehash.dhash(_REF_IMAGE)

    def __init__(self, dna = BitArray(""), rand_bit = True): 
        if rand_bit:
            self.DNA =  BitArray(bin(random.randint(0,2**circle_org.DNA_LENGTH -1)))
        else:
            self.DNA = dna
        self.image = Image.new('RGB', circle_org._REF_IMAGE.size, "white")
        
        if circle_org._IMAGE_MODE == 'RGBA':     
            self.image = Image.new('RGB', circle_org._REF_IMAGE.size, "white")
            self.img_editor = ImageDraw.Draw(self.image, 'RGBA')
        elif circle_org._IMAGE_MODE == 'L': 
            self.image = Image.new('L', circle_org._REF_IMAGE.size, "white")
            self.img_editor = ImageDraw.Draw(self.image, 'L')
        
        self.__interpret_DNA__()
        self.fit_score = self.__calc_fitness_score__()

    def save_image(self, name):
        self.image.save(name)
    
    @staticmethod
    def set_ref_image(img_name):
        circle_org._REF_IMAGE = Image.open(img_name)

    def __chunks__(self, l, total, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, total, n):
            yield l[i:i+n]
            #thanks http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python

    def __calc_fitness_score__(self):
        raw_error_acc = 0
        #RGBA multithreading has not been implemented yet
        if circle_org._IMAGE_MODE == 'RGBA':
            for new,orig in zip(circle_org._REF_IMAGE_DATA, self.image.getdata()):
                for new_col, orig_col in zip(new, orig):
                    raw_error_acc += abs(new_col - orig_col)
            return 100000/raw_error_acc

        #for new,orig in zip(circle_org._REF_IMAGE_DATA, self.image.getdata()):
        #        raw_error_acc += abs(new - orig)
        #print(raw_error_acc)
        
        l1 = list(self._REF_IMAGE_DATA)
        l2 = list(self.image.getdata())
        p = Pool(multiprocessing.cpu_count())
        split = round(self._REF_IMAGE.width / multiprocessing.cpu_count())
        total_pixels = self._REF_IMAGE.width * self._REF_IMAGE.height
        l1cols = self.__chunks__(l1, total_pixels, split)
        l2cols = self.__chunks__(l2, total_pixels, split)
        result = sum(list(p.map(calc_l, zip(l1cols, l2cols))))
        #print(result)
        p.close() #clean up processes
        p.join()
        #TODO fix this normalization...LOL
        return 100000/result
        
    def __interpret_DNA__(self):
        #c represent sthe shift
        circles = []
        for c in range(0, circle_org._CIRC_COUNT):
            shift = circle_org._CIRC_BIT_COUNT * c
            x = self.DNA[shift:shift+circle_org.X_BIT_COUNT].uint
            shift += circle_org.X_BIT_COUNT

            y = self.DNA[shift:shift+circle_org.Y_BIT_COUNT].uint
            shift += circle_org.Y_BIT_COUNT 
            
            z = self.DNA[shift:shift+circle_org.Z_BIT_COUNT].uint
            shift += circle_org.Z_BIT_COUNT 
 
            r = self.DNA[shift:shift+circle_org.R_BIT_COUNT].uint
            shift += circle_org.R_BIT_COUNT
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
                circles.append((x,y,z,r,L))
            else:
                #TODO ERROR HANDLING!
                return
            sorted(circles, key = itemgetter(2)) #sort by z value
            for c in circles:
                x = c[0]
                y = c[1]
                z = c[2]
                r = c[3]
                color = c[4]
                self.img_editor.ellipse([(x - r, y - r), (x+r, y+r)], color, color)

