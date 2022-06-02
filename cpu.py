import sys
sys.path.insert(0, './memory')
from memory import Memory 
import helper_functions

class CPU:
    def __init__(self):
        # TODO: init registers
        
        # initialize memory with 2048 words
        self.memory = Memory(2048)
        
        # no input program loaded yet
        self.is_loaded = 0
        
        # init values
        self.total_program_lines = 0
        self.current_execution_line = 0
        
    def load_program(self,filename):
        # TODO: parse input txt file and load instructions into memory 
        # default: load input program beginning at mem location ____ TODO: decide where we want to load into mem, using a random number now
        file = open(filename, 'r')
        Lines = file.readlines()
        
        for line in Lines:
            self.total_program_lines += 1
            line = line.split()
            print("storing {} at {}".format(line[1], line[0]))
            
            location = helper_functions.hex_to_decimal(line[0])
            
            # TODO: decide if we want to store value as decimal, bit array, etc.
            Memory.store_memory_value(self.memory, location, line[1])
    
        file.close()
        
        # init line of input program that we are currently executing
        self.current_execution_line = 0
        
        # set flag that we have a valid loaded program ready to execute
        self.is_loaded = 1
        
        helper_functions.print_memory_contents(self.memory)
        
    # "step" button clicked, step to next line of program and execute it 
    def step_through(self):
        self.current_execution_line += 1
        
        # if we've reached the last instruction from the input program, reset back to beginning
        if self.current_execution_line == self.total_program_lines:
            self.current_execution_line = 0
        
        # TODO: calls for executing instruction in memory
        return 
    
    # "run" button clicked, run through entire program 
    def run_program(self): 
        # no program loaded to execute, give error message 
        if not self.is_loaded:
            # TODO: throw error message in GUI
            return
        
        else:
            for i in range(self.total_program_lines):
                step_through(self)
        
        # return current line to beginning of program so we can run again 
        self.current_execution_line = 0
        return
                