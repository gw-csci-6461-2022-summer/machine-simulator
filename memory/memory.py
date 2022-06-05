# defining class memory 
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