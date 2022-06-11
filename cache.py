import sys
sys.path.insert(0, './memory')
from memory import Memory 

# cache line is the block of memory that is transferred to a memory cache. 
# The basic unit for cache storage and it may contain multiple words 
class CacheLine:
    def __init__(self, tag, value, modified):
        # tag is a unique identifier for a cache line 
        self.tag = tag
        self.value  = value
        self.modified = modified

class Cache:
    def __init_(self, size, memory, cached_data):
        self.size = size
        self.cached_data = []
        self.memory = Memory(2048)

    # checking of the tag is in the cache
    def search_tag(self, address):
        for line in self.cached_data:
            if line.tag == address:
                return True
            return False
    
    # getter for the data if the tag exists. If not we need to read from memory
    def get_data(self, address):
        for line in self.cache_content:
            if line.tag == address:
                print('Tag :',line.tag)
                print(' Cache value is :',line.value)
                # tag is present, so we return the value
                return line.value
            # tag does not exist, we go back to memory and get the data
        value = self.get_memory_value(address)
        print('Data is not in the cache. Going back to memory')
        # add the data to the cache
        new_cache_line = CacheLine(address, value)
        # we need to discuss the type of data structure we will use for cache
        self.__push(new_cache_line)
        print('we added data to the cache!')
        return value

    
    '''
    TODO
    - we might have to decide the replacement policy
    - discuss the type of data structure we will use for cache

    Maybe write code the below functions?
    - def set_data(self,address):
    - def display_cache_content(): 

    '''






