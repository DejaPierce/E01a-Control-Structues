#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # it is printing out greetings
colors = ['red','orange','yellow','green','blue','violet','purple']  # this is the list of colors that the program is going to use
play_again = '' #play_again equals what ever the color is in the list
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): # the code is saying that play_again equals n and play_again equals no
    match_color = random.choice(colors) #match_color equals random choice and the random choice has to be a color
    count = 0 # this is the number that the porgram will start with 
    color = '' # color equals '' which means that color equals play_again
    while (color != match_color): # This line is saying that color equals match_color which makes everything equal play_again
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # colors will be removed in the list in order to find the correct answer/color
        count += 1 # This means that the count or color goes up by one 
        if (color == match_color): # If the color equals Match_color
            print('Correct!') # then you are correct and the program will print out correct
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # if color does not equal match_color then you have to try again and the program will tell you have many times you have guessed 
    print('\nYou guessed it in {0} tries!'.format(count)) # The program will print out the number of tries to took for you to guess the right color
    if (count < best_count):  # if count is less then best_count
        print('This was your best guess so far!') # This was your best guess so far will print out if count < best_count
        best_count = count # best_count equals count 
    play_again = input("\nWould you like to play again? ").lower().strip() #if your guess is not correct then the program will ask if you want to play again 
print('Thanks for playing!')  #If yoy are right then the program will say thanks for playing