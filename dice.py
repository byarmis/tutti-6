from machine import Pin
from random import randint
import itertools

button = Pin(0, Pin.IN, Pin.PULL_DOWN)

'''
A = 10; 14
B = 11; 15
C = 21; 17
D = 22; 18
E = 26; 19
F = 9; 13
G = 8; 12
'''

LEFT = {
    1: [11, 21],
    2: [10, 11,  8, 26, 22],
    3: [10, 11, 21, 22,  8],
    4: [ 8, 11,  9, 21],
    5: [10,  8, 9, 21, 22],
    6: [10, 21, 22, 26,  8, 9],
}
ALL_LEFT = set(itertools.chain(*LEFT.values()))

RIGHT = {
    1: [15, 17],
    2: [14, 15, 12, 19, 18],
    3: [14, 15, 17, 18, 12],
    4: [13, 15, 12, 17],
    5: [14, 13, 12, 17, 18],
    6: [14, 17, 18, 19, 13, 12],
}
ALL_RIGHT = set(itertools.chain(*RIGHT.values()))

def reset(d):
    for p in d:
        pin = Pin(p, Pin.OUT)
        pin.low()

def display(pins):
    for p in pins:
        pin = Pin(p, Pin.OUT)
        pin.high()
    
def display_nums(a, b):
    reset(ALL_LEFT)
    display(LEFT[a])
    reset(ALL_RIGHT)
    display(RIGHT[b])    

while True:
#     import time
#     
#     for a in range(1, 7):
#         for b in range(1, 7):
#             display_nums(a, b)
#             time.sleep(.1)
    
    if button.value():
       a = randint(1, 6)
       b = randint(1, 6)
       display_nums(a, b)