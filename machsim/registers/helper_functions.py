import sys
sys.path.insert(0, './memory')
# from memory import Memory 
# import numpy as np

# convert hex string to decimal number 
def hex_to_decimal(value):
    return int(value, 16)

# print out mem contents only for locations where value is not 0
# def print_memory_contents(Memory):
#     for i in range(Memory.get_memory_size()):
#         val = Memory.get_memory_value(i)
#         if val is not 0:
#             print("Memory location {} has value {}".format(i,val))
#     return

# convert decimal to bit array of specified size (unsigned)
def decimal_to_bit_array_unsigned(value, size):
    bit_array = [int(digit) for digit in bin(value)[2:]]
    
    # add padding to make it 'size' bits long
    while len(bit_array) < size:
        bit_array.insert(0,0)
    return bit_array

# convert decimal to bit array of specified size (signed)
def decimal_to_bit_array_signed(value, size):
    bit_array = [int(digit) for digit in bin(value)[2:]]
    signed_bit = bit_array[0]
    
    # add padding to make it 'size' bits long
    while len(bit_array) < size:
        bit_array.insert(0,signed_bit)
    return bit_array
    
# convert binary to decimal 
def binary_to_decimal(value):
    value = str(value)
    return int(value,2) 

