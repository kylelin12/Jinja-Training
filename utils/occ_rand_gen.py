import csv, random

def percent_chance(dictionary):
    while True:
        for key, value in dictionary.items(): # For loop that goes through each value for each key in the dictionary
            #print chance
            ran_num = random.random() * 99.8 # Generates a random number between [0, 1) * total chance.
            #print ran_num
            if ran_num <= value:
                #print key
                return key
