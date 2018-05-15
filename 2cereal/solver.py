#!/usr/bin/python3

# Written by Zachery Ellis (TopHat)
# Solver for 2cereal from the UNSW K17 Spring CTF 2017

import os, sys, re, binascii
ACCESS_TO_FILE = True
if ACCESS_TO_FILE:
	challenge = __import__('2cereal')
TRIES = 45

# stolen from https://stackoverflow.com/questions/1323364
def special_match(strg, search=re.compile(r'[^01]').search):
	return not bool(search(strg))

# give us a file to work with 
# (We have access to the code of the challenge but otherwise you can just nc to the port it's hosted on)
def print_challenge(filename):
	if ACCESS_TO_FILE:
		sys.stdout = open(filename, "w")
		for whatever in range(0, TRIES):
			challenge.main()
		sys.stdout = sys.__stdout__
	else:
		print("netcat not implemented yet, sorry") 
		#Do the netcat stuff

# go through the file and find most common char in each spot
def solve_challenge(filename):
	char_array = []
	i = 0
	first_pass = True
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if (special_match(line)):
				if (first_pass):
					char_array.append([])
					for j in range(0,8):
						char_array[i].append(int(line[j]))

				else:
					for j in range(0,8):
						char_array[i][j] += int(line[j])
				i += 1
			elif line == "<END TRANSMISSION>":
				if (first_pass):
					first_pass = False
				i = 0
	
	final_string = ''
	for row in char_array:
		binstring = ''
		for element in row:
			if (element/TRIES >= 0.5):
				binstring += "1"
			else:
				binstring += "0"
		final_string += str(chr(int('0b'+binstring, 2)))
	print(final_string)

def main():
	file = "cereal.out"
	try:
		os.remove(file)
	except:
		None	
	print_challenge(file)
	solve_challenge(file)
	os.remove(file)

if __name__ == "__main__":
    main()