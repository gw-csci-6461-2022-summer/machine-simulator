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
        self.rx = []
        self.ry = []

    # figuring out the string that corresponds to every instruction attribute 
    def split_instruction(self):
        self.opcode = self.instruction_value[:6]
        self.index_gpr = self.instruction_value[6:8]
        self.index_ixr = self.instruction_value[8:10]
        self.indirect_addressing = self.instruction_value[10]
        self.address = self.instruction_value[11:]
        return self.opcode, self.index_gpr,self.index_ixr, self.indirect_addressing, self.address
    
    # get rx for opcodes 20 - 25 (reg to reg ops) 
    def get_rx(self):
        self.rx = self.instruction_value[6:8]
        if self.rx == str('00') : return 0 
        elif self.rx == str('01') : return 1
        elif self.rx == str('10') : return 2 
        elif self.rx == str('11') : return 3
    
    # get ry for opcodes 20 - 25 (reg to reg ops) 
    def get_ry(self):
        self.ry = self.instruction_value[8:10]
        if self.ry == str('00') : return 0 
        elif self.ry == str('01') : return 1
        elif self.ry == str('10') : return 2 
        elif self.ry == str('11') : return 3

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
            self.execute_halt()
            return 0
        elif self.opcode == 1:
            print ('Instruction: LDR')
            self.execute_loadR()
            return 1
        elif self.opcode == 2:
            print ('Instruction: STR')
            self.execute_store()
            return 2
        elif self.opcode == 3:
            print ('Instruction: LDA')
            self.execute_loadA()
            return 3
        elif self.opcode == 20:
            print ('Instruction: MLT')
            self.execute_mlt()
            return 20
        elif self.opcode == 21:
            print ('Instruction: DVD')
            self.execute_dvd()
            return 21
        elif self.opcode == 22:
            print ('Instruction: TRR')
            self.execute_trr()
            return 22
        elif self.opcode == 23:
            print ('Instruction: AND')
            self.execute_and()
            return 23
        elif self.opcode == 24:
            print ('Instruction: ORR')
            self.execute_orr()
            return 24
        elif self.opcode == 25:
            print ('Instruction: NOT')
            self.execute_not()
            return 25
        
    def get_r_val(self, gpr_index): 
        if gpr_index == 0:
            value = self.cpu.gpr0.get_value()
        elif gpr_index == 1:
            value = self.cpu.gpr1.get_value()
        elif gpr_index == 2:
            value = self.cpu.gpr2.get_value()
        else:
            value = self.cpu.gpr3.get_value()
        
        return value
      
    # multiply register by register (c(rx) * c(ry))
    # rx must be 0 or 2; ry must 0 or 2      
    def execute_mlt(self):
        # if rx or ry not 0 or 2, don't do instruction 
        rx = self.get_rx()
        if (rx != 0 or rx != 2): 
            print("invalid mult op!")
            return
        ry = self.get_ry()
        if (ry != 0 or ry != 2): 
            print("invalid mult op!")
            return
        
        # TO DO 
    
    # rx, rx+1 <- c(rx) / c(ry) 
    # rx & ry must be either 0 or 2
    # rx contains quotient; rx+1 contains remainder
    # if c(ry) = 0, set cc(3) to 1 (set DIVZERO flag)
    def execute_dvd(self):
        # rx 
        gpr_index = self.get_rx()
        print("RX", gpr_index)
        rx_val = self.get_r_val(gpr_index)
        if (isinstance(rx_val, str)):
            rx_val = helper_functions.binary_to_decimal(rx_val)
            
        if (gpr_index != 0 or gpr_index != 2): 
            print("invalid DVD inst")
            return
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
        
        if (gpry_index != 0 or gpry_index != 2): 
            print("invalid DVD inst")
            return
        
        if ry_val == 0:
            print("Divide by 0!")
            # TO DO: set cc(3) to 1
            return
        
        # get quotient 
        q = rx_val // ry_val
        remainder = rx_val % ry_val
        
        if gpr_index == 0:
            self.cpu.gpr0.set_value(q)
            self.cpu.gpr1.set_value(remainder)
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(q)
            self.cpu.gpr3.set_value(remainder)
        
        return
    
    # if c(rx) = c(ry), set cc(4) to 1; else set cc(4) to 0
    def execute_trr(self):
        # rx 
        gpr_index = self.get_rx()
        print("RX", gpr_index)
        rx_val = self.get_r_val(gpr_index)
        if (isinstance(rx_val, str)):
            rx_val = helper_functions.binary_to_decimal(rx_val)
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
            
        if rx_val == ry_val:
            print("set cc(4) to 1")
            # TO DO 
        else:
            print("set cc(4) to 0")
            # TO DO
        return
    
    # c(rx) <- c(rx) AND c(ry)
    def execute_and(self):
        # rx 
        gpr_index = self.get_rx()
        print("RX", gpr_index)
        rx_val = self.get_r_val(gpr_index)
        if (isinstance(rx_val, str)):
            rx_val = helper_functions.binary_to_decimal(rx_val)
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
        
        and_val = rx_val & ry_val
        print("result of or", and_val)
        
        if gpr_index == 0:
            self.cpu.gpr0.set_value(and_val)
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(and_val)
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(and_val)
        else:
            self.cpu.gpr3.set_value(and_val)
        
        return
    
    # c(rx) <- c(rx) OR c(ry)
    def execute_orr(self):
        # rx 
        gpr_index = self.get_rx()
        print("RX", gpr_index)
        rx_val = self.get_r_val(gpr_index)
        if (isinstance(rx_val, str)):
            rx_val = helper_functions.binary_to_decimal(rx_val)
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
        
        or_val = rx_val | ry_val
        print("result of or", or_val)
        
        if gpr_index == 0:
            self.cpu.gpr0.set_value(or_val)
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(or_val)
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(or_val)
        else:
            self.cpu.gpr3.set_value(or_val)
        
        return
    
    # c(rx) <-- Logical NOT c(rx)
    def execute_not(self):
        # rx 
        gpr_index = self.get_rx()
        print("Negating GPR", gpr_index)
        
        if gpr_index == 0:
            rx = self.cpu.gpr0.get_value()
            if (isinstance(rx, str)):
                rx = helper_functions.binary_to_decimal(rx)
            print(rx)
            rx = rx ^ 0xFFFF
            print(rx)
            self.cpu.gpr0.set_value(rx)
        elif gpr_index == 1:
            rx = self.cpu.gpr1.get_value()
            if (isinstance(rx, str)):
                rx = helper_functions.binary_to_decimal(rx)
            print(rx)
            rx = rx ^ 0xFFFF
            print(rx)
            self.cpu.gpr1.set_value(rx)
        elif gpr_index == 2:
            rx = self.cpu.gpr2.get_value()
            if (isinstance(rx, str)):
                rx = helper_functions.binary_to_decimal(rx)
            print(rx)
            rx = rx ^ 0xFFFF
            print(rx)
            self.cpu.gpr2.set_value(rx)
        else:
            rx = self.cpu.gpr3.get_value()
            if (isinstance(rx, str)):
                rx = helper_functions.binary_to_decimal(rx)
            print(rx)
            rx = rx ^ 0xFFFF
            print(rx)
            self.cpu.gpr3.set_value(rx)
        
        return
        
    def execute_halt(self):
        # stop running program
        self.cpu.HLT = 1
        return
                    
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
    
    def execute_loadR(self):
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
      
    def execute_loadA(self):
        # get effective address
        effective_address = self.load()
        print('testing load')
        print('value of EA :',effective_address)
        # TODO: check please - is this the rest of logic for load
        # Write address to MAR
        self.cpu.mar.set_value(effective_address)
        print('value set in mar',self.cpu.mar.get_value())
        
        # read from memory at location equal value at MAR
        self.cpu.mbr.set_value(self.cpu.mar.get_value())
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        
        # for LDR, load value from EA into target GPR
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
        self.cpu.mbr.set_value(value)
        print(self.cpu.mbr.get_value())
        
        # read from memory at location equal value at MAR
        self.memory.store_memory_value(self.cpu.mar.get_value(), self.cpu.mbr.get_value())
        print(value)
        print('value stored from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        print(self.memory.get_mem()[31])
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
    

