#!/usr/bin/python3

# Written by Zachery Ellis (TopHat)
# For the UNSW K17 Spring CTF 2017

import random

opening_message = """H3y th%s coNNect!on i$ a -ittle bitgarb|ed
s0 i wll tr@nsm^t th. fL@g bUT yo- miGHt nE3d t0 c0recT suM 3RR0rs 
h3R3 g-e$"""

flag = """flag{M@jor_T0m_YouR_c1rCuiT$_DEAD_ther3's_som3thing_wr0nG!}"""


closing_message = "<END TRANSMISSION>"

#If True, will not print opening message and will show original character before corrupton 
DEMO=False
NUM_TO_CORRUPT=2

#Flips NUM_TO_CORRRUPT bits in the byte
def corrupt_bin(string, bits):
    str_list = list(string)
    for num in random.sample(range(0,8), bits):
        if (str_list[num] is '0'):
            str_list[num] = '1'
        else:
            str_list[num] = '0'
    string = "".join(str_list)
    return string

#For each char in flag, ASCII to binary, then flip NUM_TO_CORRUPT bits
def main():
    if not DEMO:
        print(opening_message)
    
    for char in flag:
        bin_string = bin(int.from_bytes(char.encode(), 'big'))[2:]
        while (len(bin_string) < 8):
            bin_string = '0' + bin_string
        corrupted = corrupt_bin(bin_string, NUM_TO_CORRUPT)
        if DEMO:
            print(char+": "+bin_string+" -> "+corrupted)
        else:
            print(corrupted)
    
    if not DEMO:
        print(closing_message)

if __name__ == "__main__":
    main()
