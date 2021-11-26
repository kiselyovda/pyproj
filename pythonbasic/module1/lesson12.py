import random
import time
import os


# number1 = random.random()
# number2 = random.random()
# number3 = random.random()

# os.system('cls')
# print(number1)
# time.sleep(1)
# print(number2)
# time.sleep(2)
# print(number3)

# print('\x1b[31mПривет!')
def print_green_str(string: str):
    print(f'\x1b[4;1;32m{string}\x1b[0m')
    

slide1 = '(^_^)'
slide2 = '(^_~)'
slide3 = '(^_^)'
slide4 = '(o_0)'
slide5 = '(0_0)'
slide6 = 'Hello'

os.system('cls')
print(slide1)
time.sleep(1)


os.system('cls')
print('\x1b[4;1;32mПривет!\x1b[0m')