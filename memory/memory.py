# defining class memory 
import sys
sys.path.append('./machine-simulator')
import helper_functions
class Memory:
    
    # defining __init__() function to assign values to object properties 
    def __init__(self, size):
        self.size = size # in words  
        
        # create mem of size w init values of 0
        self.mem = {}
        for i in range(size):
            self.mem[i] = 0

    # getter for memory size  
    def get_memory_size(self):
        return self.size

    # return value at mem location, word addressable 
    def get_memory_value(self, word):
        return self.mem[word]
    
    # store value at mem location:
    def store_memory_value(self, word, value):
        self.mem[word] = value

    # reset memory to 0s
    def reset_memory(self):
        for i in range(self.size):
            self.mem[i] = 0
    
    def get_mem(self):
      return self.mem

    def read_mem(self, fileName):
        with open(fileName, 'r') as f:
            lines = f.readlines()
            if len(lines) > self.size:
                return 'Memory file too large'  # is this right? or should I only consider the valid instructions
            for line in lines:
                if line.startswith('#'):
                    continue
                addr, val = line.split(' ')[:2]
                # convert hex to interger and store at this index, the value should be integer?
                addr = helper_functions.hex_to_decimal(addr)
                val = helper_functions.hex_to_decimal(val)
                # if val >= 2**6: #we assumed the address space is the integer space
                #     self.instructions[addr] = val
                # else:
                #     self.data[addr] = val
                self.words[addr] = val