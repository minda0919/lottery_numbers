# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 02:06:31 2023

@author: Minda


This is a program that generates Lotto 6/49 numbers, based on In-Class Exercise #3 from MGTC28.
Users may use the generated numbers to pick ticket numbers when buying lottery tickets.

lottery_numbers.py uses the random library to generate numbers.


Current functionality:
    - Generate random numbers for one or more draws

Possible future functionality:
    - Predict next winning numbers
"""

import random as rd

def test(x):
    return x + 1


def gen_lotto_nums(num):
    current_num = 1
    
    all_draws = []
    
    while current_num <= num:
        current_draw = []
        
        if current_num == 1:
            last_draw = []
        
        num_pool = list(range(1, 50))
        
        if last_draw != []:
            for index in num_pool:
                for index in last_draw:
                    num_pool.remove(index)
        
        current_draw = rd.sample(num_pool, 6)
        last_draw = current_draw
        all_draws.append(current_draw)
        
    return all_draws


def print_draws(all_draws, num_draws):
    if num_draws == 1:
        print("Here are the numbers generated from your draw:")
    else:
        print("Here are the numbers generated from your", num_draws, "draws:")

    for draw in all_draws:
        print("[", draw, "]")
        print("")


while True:
    try:
        num_draws = int(input("Please input the number of draws to do: "))

        if num_draws < 0:
            print("Nice try, but you can't break my program that easily!")
            print("")
            continue
        elif num_draws == 0:
            print("Good for you!")
            print("Gambling addictions are serious. I read once that you're more likely to die on the way to buying a lottery ticket than you are to win the lottery.")
            print("")
            print("Thanks for trying out my program!")
            print("Terminating...")
            break
        else:
            draws = test(num_draws)
            print_draws(gen_lotto_nums(num_draws), num_draws)
            
            while True:
                print("")
                cont = str(input("Would you like to draw more numbers? [y/n] "))
                
                if cont == 'n' or cont == 'N':
                    print("")
                    print("Thanks for trying out my program!")
                    print("Terminating...")
                    break
                elif cont == 'y' or cont == 'Y':
                    break
                else:
                    print("Please type y or n.")
    except:
        print("Please input an integer.")
        print("")
        continue

    if cont == 'y' or cont == 'Y':
        continue
    
    break