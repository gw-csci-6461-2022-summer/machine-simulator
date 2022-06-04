import sys
sys.path.insert(0, './memory')
sys.path.insert(0, './Registers')
sys.path.insert(0, './decoder')
from memory import Memory 
from instruction import Instruction
import helper_functions
from Registers.TemplateRegister import Register
from Registers.indexRegister import indexRegister
from Registers.pc import pc
from Registers.mar import mar
from Registers.gpr import gpr 
from Registers.mbr import mbr 
from Registers.mfr import mfr
from Registers.instructionRegister import instructionregsiter


class CPU:
    def __init__(self):
        # init registers. Note that gpr and ixr have register number attribute starting from zero
        self.pc = pc('pc',12,0)
        self.gpr0= gpr('gpr',16,1,0)
        self.gpr1= gpr('gpr',16,1,1)
        self.gpr2= gpr('gpr',16,1,2)
        self.gpr3= gpr('gpr',16,1,3)
        self.ixr1= indexRegister('ixr',16,1,0)
        self.ixr2= indexRegister('ixr',16,1,1)
        self.ixr3= indexRegister('ixr',16,1,2)
        self.pc = pc('pc',12,0)
        self.mar= mar('mar',12,0)
        self.mbr= mbr('mbr',4,0)
        self.mfr = mfr('mfr',4,0)
        self.ir = instructionregsiter('ir',16,0)
       
        # initialize memory with 2048 words
        self.memory = Memory(2048)
        
        # no input program loaded yet
        self.is_loaded = 0
        
        # init values
        self.total_program_lines = 0
        self.current_execution_line = 0
        
    def load_program(self,filename):
        # default: load input program beginning at default mem location 10
        file = open(filename, 'r')
        Lines = file.readlines()
        
        for line in Lines:
            self.total_program_lines += 1
            line = line.split()
            print("storing {} at {}".format(line[1], line[0]))
            
            location = helper_functions.hex_to_decimal(line[0])
            
            # TODO: decide if we want to store value as decimal, bit array, etc.
            Memory.store_memory_value(self.memory, location, helper_functions.hex_to_decimal(line[1]))
    
        file.close()
        
        helper_functions.print_memory_contents(self.memory)
        
    # "step" button clicked, step to next line of program and execute it 
    def step_through(self):
        print("stepping")
        
        # copy address from PC to MAR
        self.mar.set_value(self.pc.get_value())
        print(self.pc.get_value())
        
        # increment pc
        self.pc.increment_pc()
        
        # load MBR with instruction/data from Memory[MAR]
        self.mbr.set_value(self.memory.get_memory_value(self.mar.get_value()))
        
        # copy mbr to ir
        self.ir.set_value(helper_functions.decimal_to_bit_array_unsigned(self.mbr.get_value(),16))
        
        # decode 
        inst = Instruction()
        inst.instruction_value = self.ir.get_value()
        inst.split_instruction()
        opcode = inst.get_opcode()
        index_gpr = inst.get_index_gpr()
        print('opcode:',inst.get_opcode())
        print('general purpose register:',inst.get_index_gpr())
        print('index register:',inst.get_index_ixr())
        print('indirect addressing:',inst.get_indirect_addressing())
        print('address: ',inst.get_address())
        print('converted opcode',int(opcode, base=2))
        print('converted gpr',int(index_gpr, base=2))
        inst.decoding_instruction()
        
        # reset pc if we're at end
        if self.pc.get_value() == ++self.memory.get_memory_size():
            self.pc.set_value(0)
        
        return 
    
    # "run" button clicked, run through entire program 
    def run_program(self): 
        for i in range(self.pc.get_value(), self.memory.get_memory_size()):
            self.step_through()
            
        return