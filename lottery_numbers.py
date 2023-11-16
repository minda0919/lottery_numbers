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
    - Allowing inputs with blank spaces, x.0 (more flexibility with inputs)
"""

# import random library
import random as rd


# function to generate lotto numbers
# num is the number of draws to do
# returns a nested list of all draws done, where each draw is a list of 6 numbers
def gen_lotto_nums(num):
    # counter to track how many draws have been done
    current_num = 1
    
    # list to store all completed draws
    all_draws = []
    
    # run the following until the specified number of draws have been done
    while current_num <= num:
        # list to store the current draw
        # on subsequent iterations, this will reset the variable
        current_draw = []
        
        # if current iteration is the first one:
        if current_num == 1:
            # list to store the previous draw, used to ensure numbers don't repeat on the next draw
            # only runs on the first iteration so it can be changed and brought forward for future iterations
            last_draw = []
        
        # list of the pool of numbers to draw from, from 1-49
        num_pool = list(range(1, 50))
        
        # if current iteration is NOT the first one:
        if last_draw != []:
            # for all numbers in last_draw:
            for number in last_draw:
                # remove those numbers from num_pool, so they don't repeat on this draw
                num_pool.remove(number)
        
        # draw 6 nonrepeating numbers out of num_pool
        current_draw = rd.sample(num_pool, 6)
        # update last_draw for the next iteration
        last_draw = current_draw
        # add this draw to the list of all draws
        all_draws.append(current_draw)
        # iterate counter
        current_num = current_num + 1
        
    return all_draws


# function to print drawn lotto numbers
# all_draws is a list of draws
def print_draws(all_draws):
    # number of draws in all_draws
    len_draws = len(all_draws)
    
    print('')
    print('')
    # if only one draw was done:
    if len_draws == 1:
        print('Here are the numbers generated from your draw:')
    # if more than one draw was done:
    else:
        print('Here are the numbers generated from your', len_draws, 'draws:')

    print('')
    # for each draw in the list:
    for draw in all_draws:
        # print the draw number
        # doesn't work properly if list has repeated numbers; not an issue if print_draws() is used with numbers generated from gen_lotto_nums()
        print('Draw', all_draws.index(draw) + 1)
        # print the draw
        print(draw)
        print('')


# main program
# run until a break is encountered:
while True:
    # error handling for non-int inputs
    try:
        # ask user to input a number
        num_draws = int(input('Please input the number of draws to do: '))

        # don't allow for negative numbers
        if num_draws < 0:
            # error message
            print('Nice try, but you can\'t break my program that easily!')
            print('')
            # restart loop
            continue
        # special message for input of zero
        elif num_draws == 0:
            print('')
            print('Good for you!')
            print('Gambling addictions are serious. I read once that you\'re more likely to die on the way to buying a lottery ticket than you are to win the lottery.')
            print('')
            print('Thanks for trying out my program!')
            print('Terminating...')
            # exit loop
            break
        # for all other valid inputs:
        else:
            # generate numbers and print them
            print_draws(gen_lotto_nums(num_draws))
            
            # run until a break is encountered:
            # option to restart the program
            while True:
                print('')
                # ask if user wants to restart program
                cont = str(input('Would you like to draw more numbers? [y/n] '))
                
                # if user inputs no:
                if cont == 'n' or cont == 'N':
                    print('')
                    print('Thanks for trying out my program!')
                    print('Terminating...')
                    # exit loop
                    break
                # if user inputs yes:
                elif cont == 'y' or cont == 'Y':
                    # exit loop
                    break
                # if user puts an invalid input:
                else:
                    print('Please type y or n as indicated.')
    # if error is encountered:
    except:
        # error message
        print('Please input an integer.')
        print('')
        # restart loop
        continue
    
    # if user wanted to restart the program:
    if cont == 'y' or cont == 'Y':
        # restart loop
        continue
    
    # exit loop; end program
    break