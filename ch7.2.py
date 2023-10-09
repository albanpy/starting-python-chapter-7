#Lottery Number Generator
from random import *
def main():
    try:
        num=7
        seed(0)
        lot_number=[0]*num
        rands(lot_number,num)
        #######################
        print(f'seven-digit lottery number are:-')
        for z in lot_number:
            print(z)    
    except Exception as d:
        print(d)  
def rands(lot_n,num):
    try:
        for n in range(num):
            lot_n[n]=randrange(0,9)
    except Exception as k:
        print(k)
main()
            

 

