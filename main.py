#!/usr/bin/python3

def decode(decode_file):
    """This function reades encoded message from  a .txt file and returns
    a decoded version as a string"""

    #open the file passed as an argument for reading
    with open(decode_file, 'r') as file:
        """declare a dictionary that will store the contents of the file                       mapping each number to a string in the text"""
        my_dict = {}
        #iterate through each and every line in the opened file
        for line in file:
            #split each line into a number and string part
            parts = line.split()
            
            key = int(parts[0])
            value = parts[1]
            #map each number in the file to its corresponding text
            my_dict[key] = value
   
    #sort the dictionaty for easy accessing of its elements
    sorted_dict = dict(sorted(my_dict.items()))
    next_key = 2
    key = 1

    #start iteration from 1 upto the last element of the dictionary
    while key <= len(sorted_dict):
        print("{}".format(my_dict[key]), end = ' ')
        key += next_key
        next_key += 1

decode('decode_file.txt')
