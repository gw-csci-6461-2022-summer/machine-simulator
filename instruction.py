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
# import cpu
from Registers.indexRegister import indexRegister
from Registers.mar import mar

class Instruction:
    # ctor
    def __init__(self, cpu, memory):
        self.instruction_value = '0' * 16 
        self.opcode = []
        self.index_gpr = []
        self.index_ixr = []
        self.indirect_addressing = []
        self.address = []
        self.memory = memory
        self.cpu = cpu

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
        if index_gpr == str('00') : return 0 
        elif index_gpr == str('01') : return 1
        elif index_gpr == str('10') : return 2 
        elif index_gpr == str('11') : return 3
    
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
            self.execute_load()
            return 1
        elif self.opcode == 2:
            print ('Instruction: STR')
            # TODO: execute_store()
            return 2
                    
    # load instruction 
    def load (self) :
        # determine which ixr to use
        index = self.get_index_ixr()
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
                if index == 1:
                    value = self.cpu.ixr1.get_value()
                elif index == 2:
                    value = self.cpu.ixr2.get_value()
                else:
                    value = self.cpu.ixr3.get_value()   
                effective_address = address + value
                print("EA is " + str(effective_address))
                
        # indirect addressing
        else :
            # case where indirect_addressing == 1 
            if index == 0:
                effective_address = self.memory.get_memory_value(address)
            # there is indexing
            elif index > 0 and index < 4:
                # calculate the effective address
                if index == 1:
                    value = self.cpu.ixr1.get_value()
                elif index == 2:
                    value = self.cpu.ixr2.get_value()
                else:
                    value = self.cpu.ixr3.get_value()
                # get fetch memory[address]
                effective_address = self.memory.get_memory_value(address + value)
                print("EA is " + str(effective_address))
        return effective_address
    
    def execute_load(self):
        # get effective address
        effective_address = self.load()
        print('testing load')
        print('value of EA :',effective_address)
        # TODO: check please - is this the rest of logic for load
        # Write address to MAR
        self.cpu.mar.set_value(effective_address)
        print('value set in mar',self.cpu.mar.get_value())
        # read from memory at location equal value at MAR
        self.cpu.mbr.set_value(self.memory.get_memory_value(self.cpu.mar.get_value()))
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        
        # for LDR, load value from mbr into target GPR
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            self.cpu.gpr0.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(self.cpu.mbr.get_value())
        else:
            self.cpu.gpr3.set_value(self.cpu.mbr.get_value())
            
        # TODO : This is needed for caching. read data from MBR (do we display this anywhere other than MBR?)
        return

    # store instruction 
    def store (self) :
        # determine which ixr to use
        index = self.get_index_ixr()
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
                if index == 1:
                # print(ixr.get_value())
                    value = self.cpu.ixr1.get_value()
                elif index == 2:
                    value = self.cpu.ixr2.get_value()
                else:
                    value = self.cpu.ixr3.get_value()
                    
                effective_address = address + value
                print("EA is " + str(effective_address))
                
        # indirect addressing
        else :
            # indirect_addressing == 1 
            if index == 0:
                # get fetch memory[address]
                effective_address = self.memory.get_memory_value(address)
            # there is indexing
            elif index > 0 and index < 4:
                # calculate the effective address
                if index == 1:
                    # print(ixr.get_value())
                    value = self.cpu.ixr1.get_value()
                elif index == 2:
                    value = self.cpu.ixr2.get_value()
                else:
                    value = self.cpu.ixr3.get_value()
                # get fetch memory[address]
                effective_address = self.memory.get_memory_value(address + value)
                # marReg.set_value(address + ixr.get_value())
                print("EA is " + str(effective_address))
        return effective_address
    
    def execute_store(self):
        # get effective address
        effective_address = self.load()
        print('testing store')
        print('value of EA :',effective_address)
        
        # Write address to MAR
        self.cpu.mar.set_value(effective_address)
        print('value set in mar',self.cpu.mar.get_value())
        
        # for STR, store value from gprx into target address
        # fetch val from target gpr
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            value = self.cpu.gpr0.get_value()
        elif gpr_index == 1:
            value = self.cpu.gpr1.get_value()
        elif gpr_index == 2:
            value = self.cpu.gpr2.get_value()
        else:
            value = self.cpu.gpr3.get_value()
        
        # read from memory at location equal value at MAR
        self.memory.store_memory_value(value, self.cpu.mbr.get_value())
        print(value)
        print('value stored from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        print(self.memory.get_mem().values()[31])
        # TODO : This is needed for caching. read data from MBR (do we display this anywhere other than MBR?)
        return



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
    

