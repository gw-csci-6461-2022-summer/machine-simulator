import sys
sys.path.insert(0, './memory')
sys.path.append('./machine-simulator')
from memory import Memory
import helper_functions

# cache line is the block of memory that is transferred to a memory cache. 
# The basic unit for cache storage and it may contain multiple words 
class Cache:
    def __init__(self, mem_ref,block_size=4,max_size=16): #16 lines, unclear block-size
        self.lines = [] #tuple array: [(tag, block)], block = [(addr, word)]
        self.max_size = max_size
        self.mem = mem_ref
        self.block_size = block_size

    def decode(self,addr):
        """_summary_

        Args:
            addr (int): 12-bit address space
        """
        b_str = helper_functions.decimal_to_binary(addr,12)
        tag = helper_functions.binary_string_to_decimal(b_str[:10])
        blocking_offset = helper_functions.binary_string_to_decimal(b_str[10:])
        return tag, blocking_offset
        
    #read
    def get_word(self,addr):
        """searches for word in cache, if not present, fetches from main memory
        copies it into cache, and returns data to caller. If the cache is full 
        We pop using FIFO and append data to the end 

        Args:
            addr (int): integer denoting memory address of word
        """
        tag, blocking_offset = self.decode(addr)
        #loop through since we don't have an idx, find matching tag
        for t, b in self.lines:
            if t == tag:
                for byte_addr, word in b:
                    if byte_addr == blocking_offset:
                        return word

        #pop if full
        if len(self.lines) == self.max_size:
            self.lines.pop(0)
        
        #get block from main memory
        block_num = addr // self.block_size
        start = block_num * self.block_size
        end = min(start + self.block_size, len(self.mem.words))
        block = [(a % self.block_size,self.mem.words[a]) for a in range(start,end)]
        self.lines.append((tag,block))
        return block[addr % self.block_size][1]

    def set_word(self,addr, new_word):
        """For writing to main memory. First we see if data is present in cache
        if it is we do a write through, else...?

        Args:
            addr (int): memory address of where instruction wants to write
            new_word (int): data to put into that memory address
        """

        #loop through cache to find the matching block (via tag),
        #  then loop to find correct word??  

        tag, offset = self.decode(addr)
        for i, (t, b) in enumerate(self.lines):
            if t == tag:
                for j, (a,word) in enumerate(b): #do we have to loop through this? can this be a dictionary?
                    if a == offset:
                        block  = self.lines[i][1]
                        block[j] = (a,new_word)
                        #write to main mem
                        self.mem.words[addr] = new_word
                        return

        #Write no-allocate
        self.mem.words[addr] = new_word
    
    def clear_cache(self):
        self.lines = []
# class CacheLine:
#     def __init__(self, tag, value, modified):
#         # tag is a unique identifier for a cache line 
#         self.tag = tag
#         self.value  = value
#         self.modified = modified

# class Cache:
#     def __init_(self, size, memory, cached_data):
#         self.size = size
#         self.cached_data = []
#         self.memory = Memory(2048)

#     # checking of the tag is in the cache
#     def search_tag(self, address):
#         for line in self.cached_data:
#             if line.tag == address:
#                 return True
#             return False
    
#     # getter for the data if the tag exists. If not we need to read from memory
#     def get_data(self, address):
#         for line in self.cache_content:
#             if line.tag == address:
#                 print('Tag :',line.tag)
#                 print(' Cache value is :',line.value)
#                 # tag is present, so we return the value
#                 return line.value
#             # tag does not exist, we go back to memory and get the data
#         value = self.get_memory_value(address)
#         print('Data is not in the cache. Going back to memory')
#         # add the data to the cache
#         new_cache_line = CacheLine(address, value)
#         # we need to discuss the type of data structure we will use for cache
#         self.__push(new_cache_line)
#         print('we added data to the cache!')
#         return value
      
#     def set_data(self, address, value):
#         if self.cached_data.len() >= 16:
#             self.cached_data.pop()
#         if self.search_tag(address):
#             new_cache_line = CacheLine(address, value)
#             self.cached_data.append(new_cache_line)
#             self.memory.store_memory_value(address, value)
#             return

    # def set(self, add : int, value : str):
    #     """This function looks for tag in cache.
    #     set both memory and cache if tag exists,
    #     set memory and push the line into cache if it doesn't
    #     """
    #     for line in self.cache_content:
    #         if line.tag == add:
    #             line.value = value
    #             self.msg = 'Update Cache[tag=' + str(add) + ']\n'
    #             self.mem.set_to_memory(add, value)
    #             self.msg += 'MEM['+str(add)+'] :\t\t\t'+str(int(value))+'\n\n'
    #             return
    #     new_line = CacheLine(add, value)
    #     self.__push(new_line)
    #     self.msg = 'Not in Cache, push into Cache\n'
    #     self.mem.set_to_memory(add, value)
    #     self.msg += 'MEM['+str(add)+'] :\t\t\t'+str(int(value))+'\n\n'

    # def print_out(self):
    #     word = '\n-------------CACHE---------------\n'
    #     for line in self.cache_content:
    #         word += str(line.tag) + ':\t' + str(int(line.value)) + '\n'
    #     return word


    
    # '''
    # TODO
    # - we might have to decide the replacement policy
    # - discuss the type of data structure we will use for cache

    # Maybe write code the below functions?
    # - def set_data(self,address):
    # - def display_cache_content(): 

    # I was thinking of using a queue for the cache. add to top with append
    # pop() removes last element if cache is full
    # We still need to have an in depth talk about the structure
    # '''

def main():
   mem = Memory(2048)
   mem.read_mem('IPL.txt')
   print(mem.words[16])
   c = Cache(mem)

   #get word test
   c.get_word(19)

if __name__ == '__main__':
    main()






