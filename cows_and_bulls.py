import random

def get_input():
    strnum = None
    while strnum is None or len(strnum) != 4:
        num = input('Give me a four digit number: ')
        if len(num) == 4:
            intnum = int(num)
            strnum = '{:04d}'.format(intnum)
    return strnum

def get_target():
    target = random.randint(0, 9999)
    strtarget = '{:04d}'.format(target)
    return strtarget

def count_cows(guess, target):
    cows = 0
    for g,t in zip(guess, target):
        if g == t:
            cows += 1
    return cows



print('Hello. Welcome to the awesome cows and bulls game!')
target = get_target()
haswon = False
while not haswon:
    
    guess = get_input() 
    cows = count_cows(guess, target)
    print('You have {} number of cows'.format(cows))

    if cows == 4:
        print('You have enough cows. You win!')
        haswon = True