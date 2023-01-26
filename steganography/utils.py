#!/usr/bin/env python3

def str2bin(string):
    binary = ''
    for char in string:
        binary += bin(
                ord(char)
            )\
            [2:]\
            .zfill(8)

    return binary

def bin2str(binary):
    integer=int(binary, 2)
    total_bytes= (integer.bit_length() +7) // 8
    bytesValue = integer.to_bytes(total_bytes, "big")
    string=bytesValue.decode()
    return string

def int2bin(integer):
    return bin(integer)[2:].zfill(8)

def bin2int(binary):
    return int(binary, 2)
