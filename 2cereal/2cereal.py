#!/usr/bin/python3

import random

opening_message = """H3y th%s coNNect!on i$ a -ittle bitgarb|ed
s0 i wll tr@nsm^t th. fL@g bUT yo- miGHt nE3d t0 c0recT suM 3RR0rs 
h3R3 g-e$"""

flag="""flag{M@jor_T0m_YouR_c1rCuiT$_DEAD_ther3's_som3thing_wr0nG!}"""

demo=True

def corrupt_bin(string, bits):
    str_list = list(string)
    for num in random.sample(range(0,8), bits):
        if (str_list[num] is '0'):
            str_list[num] = '1'
        elif (str_list[num] is '1'):
            str_list[num] = '0'
    string = "".join(str_list)
    return string

def main():
    if not demo:
        print(opening_message)
    for char in flag:
        bin_string = bin(int.from_bytes(char.encode(), 'big'))[2:]
        while (len(bin_string) < 8):
            bin_string = '0' + bin_string
        corrupted = corrupt_bin(bin_string, 2)
        if demo:
            print(char+": "+bin_string+" -> "+corrupted)
        else:
            print(corrupted)

if __name__ == "__main__":
    main()
