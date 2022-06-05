'''steps for decoding an instruction 
1 - create an object instruction 
2 - read instruction from instruction register
3-  use setters to set the values that are read in object instruction 
4 - use getters the read value form object instruction '''

import sys
sys.path.insert(0, './memory')
sys.path.insert(0, './Registers')
import helper_functions
from memory import Memory
import cpu
from Registers.indexRegister import indexRegister
from Registers.mar import mar

class Instruction:
    # ctor
    def __init__(self):
        self.instruction_value = '0' * 16 
        self.opcode = []
        self.index_gpr = []
        self.index_ixr = []
        self.indirect_addressing = []
        self.address = []

    # figuring out the string that corresponds to every instruction attribute 
    def split_instruction(self):
        self.opcode = self.instruction_value[:6]
        self.index_gpr = self.instruction_value[6:8]
        self.index_ixr = self.instruction_value[8:10]
        self.indirect_addressing = self.instruction_value[10]
        self.address = self.instruction_value[11:]
        return self.opcode, self.index_gpr,self.index_ixr, self.indirect_addressing, self.address

    # defining getters to access instruction attributes 
    def get_opcode(self):
        opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return opcode
    
    def get_index_gpr(self):
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.index_gpr
    
    def get_index_ixr(self):
        opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        if index_ixr == str('00') : return 0 
        elif index_ixr == str('01') : return 1
        elif index_ixr == str('10') : return 2 
        elif index_ixr == str('11') : return 3
    
    def get_indirect_addressing(self):
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.indirect_addressing

    def get_address(self):
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.address
    
    def decoding_instruction(self):
        # calculate opcode
        self.opcode = int(str(self.opcode),base=2)
        if self.opcode == 0:
            print ('Instruction: HALT')
            # TODO: execute_halt()
            return 0
        elif self.opcode == 1:
            print ('Instruction: LDR')
            # TODO: execute_load()
            return 1
        elif self.opcode == 2:
            print ('Instruction: STR')
            # TODO: execute_store()
            return 2

    # load instruction 
    def load (self, ixr: indexRegister, marReg: mar, mem: Memory) :
        mem.get_memory_value()
        index = ixr.get_ixr_number()
        address = helper_functions.binary_to_decimal(self.address)
        print('index:', index)
        effective_address = 0
        # no indirect addressing 
        if (self.indirect_addressing == '0') :
            # no indexing
            if index == 0:
                # the effective address is the address itself
                effective_address = address
                print("EA where index is 0 is " + str(effective_address))
            # there is indexing
            elif index > 0 and index < 4:
                # calculate the effective address
                # change the ixr in cpu
                # TODO check again this logic. I need to access data [indexRegister][self.get_index_ixr].value()
                print(ixr.get_value())
                effective_address = address + ixr.get_value() 
                print("EA is " + str(effective_address))
                
        # indirect addressing
        else :
            # indirect_addressing == 1 
            if index == 0:
                # check memory 
                # mar.set_value(InstructionRegister.get_value)
                effective_address = address
                marReg.set_value(address)
            # there is indexing
            elif index > 0 and index < 4:
                # calculate the effective address
                # TODO check again this logic. I need to access data [indexRegister][self.get_index_ixr].value()
                effective_address = address + ixr.get_value()
                marReg.set_value(address + ixr.get_value())
                print("EA is " + str(effective_address))
        return effective_address




'''You need instrcution and memory adress
Load MBR to see entire instruction in MBR
MBR shows instruction as binary string
Load MAR with addess
Instruction from MBR will be loaded in MAR
MAR incremented by 1

2 ways to load into memory (init and LD)

After loading into memory 
we assign to PC the first address and increase pc by 1
load PCto run 
after that we run single step - execute, copy instruction to IR  and increase
it will put values in MAR and MBR'''
    

