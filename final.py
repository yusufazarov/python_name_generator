# Name Generator by Yusuf Azarov
# About: This code will randomly pick a male/female/non gender fake name for you to use online

import sys
# this will be used to shutdown my code

import random
def random_line(fname):
        lines = open(fname).read().splitlines()
        return random.choice(lines)
# this function will randomly pick a line from a txt file that I'll be using
# fname stands for filename, it will open a file from which it will drag a line and print it


#where did we get the name files...
#http://scrapmaker.com/data/wordlists/names/surnames.txt

genderChoice = input("please type: male or female or n --for non gendered--  ")
# this will be the user input

if genderChoice == "male":
        print("The random generated male name is ... ")
        print(random_line('male.txt'))
elif genderChoice == "female":
        print("The random generated female name is ... ")
        print(random_line('female.txt'))
elif genderChoice == "n":
        print("The random generated non gendered name is ... ")
        print(random_line('both.txt'))
else:
        print("please restart the code and type in: male, female or n")
        sys.exit()
        

lastName = input("would you also like a last name? (yes or no) ")
if lastName == "yes":
        print("The random generetard last name is ... ")
        print(random_line('lname.txt'))
elif lastName == "no":
        print("Thanks for using my code!")
else:
        print("please restart the code and type: yes or no")
        sys.exit()
