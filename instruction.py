'''steps for decoding an instruction 
1 - create an object instruction 
2 - read instruction from instruction register
3-  use setters to set the values that are read in object instruction 
4 - use getters the read value form object instruction '''

from functools import cache
import sys
sys.path.insert(0, './memory')
sys.path.insert(0, './Registers')
import helper_functions
from memory import Memory
from cache import Cache
# import cpu
from Registers.indexRegister import indexRegister
from Registers.mar import mar

class Instruction:
    # ctor
    def __init__(self, cpu, memory, cache):
        self.instruction_value = '0' * 16 
        self.opcode = []
        self.index_gpr = []
        self.index_ixr = []
        self.indirect_addressing = []
        self.address = []
        self.memory = memory
        self.cache = cache
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
        elif self.opcode == 10:
            print ('Instruction: JZ')
            self.execute_jump_if_zero()
            return 10
        elif self.opcode == 11:
            print ('Instruction: JNE')
            self.execute_jump_if_not_equal()
            return 11
        elif self.opcode == 12:
            print ('Instruction: JCC')
            self.execute_jump_if_condition_code()
            return 12
        elif self.opcode == 13:
            print ('Instruction: JMA')
            self.execute_unconditional_jump_to_address()
            return 13
        elif self.opcode == 14:
            print ('Instruction: JSR')
            self.execute_jump_and_save_return_address()
            return 14
        elif self.opcode == 15:
            print ('Instruction: RFS')
            self.execute_return_from_subroutine()
            return 15
        elif self.opcode == 16:
            print ('Instruction: SOB')
            self.execute_subtract_one_and_branch()
            return 16
        elif self.opcode == 17:
            print ('Instruction: JGE')
            self.execute_jump_greater_than_or_equal_to()
            return 17
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
        # rx 
        gpr_index = self.get_rx()
        print("RX", gpr_index)
        rx_val = self.get_r_val(gpr_index)
        if (isinstance(rx_val, str)):
            rx_val = helper_functions.binary_to_decimal(rx_val)
            
        if (gpr_index != 0 and gpr_index != 2): 
            print("invalid MLT inst")
            return
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
        
        if (gpry_index != 0 and gpry_index != 2): 
            print("invalid MLT inst")
            return
        
        print("RX val", rx_val)
        print("RY val", ry_val)
        
        mlt_val = rx_val * ry_val
        
        mlt_val = bin(mlt_val)
       
        high_order_bits = mlt_val[:len(mlt_val)//2]
        low_order_bits = mlt_val[len(mlt_val)//2:]
        print(high_order_bits)
        print(low_order_bits)
        
        high_order_bits = helper_functions.binary_to_decimal(high_order_bits[2:].zfill(16))
        low_order_bits = helper_functions.binary_to_decimal(low_order_bits.zfill(16))
        
        print("high order:", high_order_bits)
        print("low order:", low_order_bits)
        
        if gpr_index == 0:
            self.cpu.gpr0.set_value(high_order_bits)
            self.cpu.gpr1.set_value(low_order_bits)
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(high_order_bits)
            self.cpu.gpr3.set_value(low_order_bits)
        
        return
        
    
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
            
        if (gpr_index != 0 and gpr_index != 2): 
            print("invalid DVD inst")
            return
        
        # ry 
        gpry_index = self.get_ry()
        print("RY", gpry_index)
        ry_val = self.get_r_val(gpry_index)
        if (isinstance(ry_val, str)):
            ry_val = helper_functions.binary_to_decimal(ry_val)
        
        if (gpry_index != 0 and gpry_index != 2): 
            print("invalid DVD inst")
            return
        
        if ry_val == 0:
            print("Divide by 0!")
            # TO DO: set cc(3) to 1
            return
        
        # get quotient 
        q = rx_val // ry_val
        remainder = rx_val % ry_val
        
        print("Quotient", q)
        print("Remainder", remainder)
        
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
        print('value of EA :',effective_address)
        
        # TODO: check please - is this the rest of logic for load
        
        # Write address to MAR
        self.cpu.mar.set_value(effective_address)
        print('value set in mar',self.cpu.mar.get_value())
        
        # read from memory at location equal value at MAR
        # self.cpu.mbr.set_value(self.memory.get_memory_value(self.cpu.mar.get_value()))
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        # read from cache at location eqaul to value at MAR
        print('value read from cache:',self.cache.get_word(self.cpu.mar.get_value()))
        self.cpu.mbr.set_value(self.cache.get_word(self.cpu.mar.get_value()))
        
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
            
        # TODO: This is needed for caching. read data from MBR (do we display this anywhere other than MBR?)

        self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())

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
        # self.cpu.mbr.set_value(self.cpu.mar.get_value())
        self.cpu.mbr.set_value(self.cache.get_word(self.cpu.mar.get_value()))
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
        self.cache.set_word(effective_address, self.cpu.mbr.get_value())
        print(self.cpu.mbr.get_value())
        
        # read from memory at location equal value at MAR
        self.memory.store_memory_value(self.cpu.mar.get_value(), self.cpu.mbr.get_value())
        print(value)
        print('value stored from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))
        print(self.memory.get_mem()[31])
        # TODO : This is needed for caching. read data from MBR (do we display this anywhere other than MBR?)
        return

    '''
        You need instrcution and memory adress
        Load MBR to see entire instruction in MBR
        MBR shows instruction as binary string
        Load MAR with addess
        Instruction from MBR will be loaded in MAR
        MAR incremented by 1

        2 ways to load into memory (init and LD)

    def execute_smr(self):
        print('SMR')
        
        # Get register content
        ea_content = self.load()
        print('value of c(EA) :',ea_content)
            
        register_content = self.store()
        print('value of C(r) :', register_content)

        effective_address = ea_content - register_content
        print(effective_address)

        # Write address to MAR
        self.cpu.mar.set_value(effective_address)
        print('value set in mar',self.cpu.mar.get_value())
        
        # read from memory at location equal value at MAR
        # fetch from cache(self.MAR.get_val())
        self.cpu.mbr.set_value(self.cache.get_word(self.cpu.mar.get_value()))
        # self.cpu.mbr.set_value(self.memory.get_memory_value(self.cpu.mar.get_value()))
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))

        # for SMR, load value from mbr into target GPR
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            self.cpu.gpr0.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(self.cpu.mbr.get_value())
        else:
            self.cpu.gpr3.set_value(self.cpu.mbr.get_value())
        
        return

    def execute_air(self):
        print('AIR')

        #get register content
        register_content = self.store()
        immed = self.get_address
    
        if immed > 0: 
            if register_content > 0:
                register_content = register_content + immed
            elif register_content == 0:
                register_content = immed
            print('value of C(r) :', register_content)
        else:
            print('Please enter immediate value')
            pass
        
        # Write address to MAR
        self.cpu.mar.set_value(register_content)
        print('value set in mar',self.cpu.mar.get_value())
        
        # read from memory at location equal value at MAR
        self.cpu.mbr.set_value(self.memory.get_memory_value(self.cpu.mar.get_value()))
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))

        # for SMR, load value from mbr into target GPR
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            self.cpu.gpr0.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(self.cpu.mbr.get_value())
        else:
            self.cpu.gpr3.set_value(self.cpu.mbr.get_value())
        
        return
    
    def execute_sir(self):
        print('SIR')

        #get register content
        register_content = self.store()
        immed = self.get_address

        if immed > 0: 
            if register_content > 0:
                register_content = register_content - immed
            elif register_content == 0:
                register_content = immed
            print('value of C(r) :', register_content)
        else:
            print('Please enter immediate value')
            pass
        
     # Write address to MAR
        self.cpu.mar.set_value(register_content)
        print('value set in mar',self.cpu.mar.get_value())
        
        # read from memory at location equal value at MAR
        self.cpu.mbr.set_value(self.memory.get_memory_value(self.cache.get_word(self.cpu.mar.get_value())))
        # self.cpu.mbr.set_value(self.memory.get_memory_value(self.cpu.mar.get_value()))
        print('value read from memory:',self.memory.get_memory_value(self.cpu.mar.get_value()))

        # for SMR, load value from mbr into target GPR
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            self.cpu.gpr0.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 1:
            self.cpu.gpr1.set_value(self.cpu.mbr.get_value())
        elif gpr_index == 2:
            self.cpu.gpr2.set_value(self.cpu.mbr.get_value())
        else:
            self.cpu.gpr3.set_value(self.cpu.mbr.get_value())
        
        return   

        After loading into memory 
        we assign to PC the first address and increase pc by 1
        load PC to run 
        after that we run single step - execute, copy instruction to IR  and increase
        it will put values in MAR and MBR
    '''
    
    # transfer instructions
    def execute_jump_if_zero(self):
        print("PC:", self.cpu.pc.get_value())
        # if c(r) = 0 
        if self.get_value_gpr() == 0:
            #PC <- EA
            self.cpu.pc.set_value(self.load())
        else: 
            self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_jump_if_not_equal(self):
        # if c(r) != 0 
        if self.get_value_gpr() != 0:
            #PC <- EA
            self.cpu.pc.set_value(self.load())
        else: 
            self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_jump_if_condition_code(self,cc_bit):
        # specifies the bit in the condition code register to check
        # if cc bit = 1
        if self.get_value_cc_bit(cc_bit) == 1:
            # PC <- EA
            self.cpu.pc.set_value(self.load())
        else: 
            self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_unconditional_jump_to_address(self):
        # PC <- EA
        self.cpu.pc.set_value(self.load())
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_jump_and_save_return_address(self):
        # R3 <- PC+1;
        self.cpu.gpr3.setvalue(self.cpu.pc.get_value()+1)
        # PC <- EA
        self.cpu.pc.set_value(self.load())
        # R0 should contain pointer to arguments
        # Argument list should end with ???1 (all 1s) value
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_return_from_subroutine(self):
        # Return From Subroutine w/ return code as Immed portion (optional) 
        # stored in the instruction???s address field. 
        # TODO R0 <- Immed
        # PC <- c(R3)
        self.cpu.pc.set_value(self.cpu.gpr3.get_value())
        return

    def execute_subtract_one_and_branch(self):
        # r <- c(r) ??? 1
        self.set_value_gpr(self.get_value_gpr - 1)
        # if c(r) > 0  
        if self.get_value_gpr > 0:
            # PC <- EA; 
            self.cpu.pc.set_value(self.load())
        else:
            self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())
        return

    def execute_jump_greater_than_or_equal_to(self):
        # if c(r) >= 0
        if self.get_value_gpr >= 0:
            # PC <- EA 
            self.cpu.pc.set_value(self.load())
        else:
            self.cpu.pc.increment_pc()
        print("PC:", self.cpu.pc.get_value())
        return

    # transfer instruction helper functions

    # get gpr value at instruction gpr index
    def get_value_gpr(self):
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            print("GPR0:", self.cpu.gpr0.get_value())
            return self.cpu.gpr0.get_value()
        elif gpr_index == 1:
            print("GPR1:", self.cpu.gpr1.get_value())
            return self.cpu.gpr1.get_value()
        elif gpr_index == 2:
            print("GPR2:", self.cpu.gpr2.get_value())
            return self.cpu.gpr2.get_value()
        else:
            print("GPR3: ", self.cpu.gpr3.get_value())
            return self.cpu.gpr3.get_value()

    
     # set gpr value at instruction gpr index
    def set_value_gpr(self,value):
        gpr_index = self.get_index_gpr()
        if gpr_index == 0:
            return self.cpu.gpr0.set_value(value)
        elif gpr_index == 1:
            return self.cpu.gpr1.set_value(value)
        elif gpr_index == 2:
            return self.cpu.gpr2.set_value(value)
        else:
            return self.cpu.gpr3.set_value(value)

    # get cc bit value
    def get_value_cc(self,cc_bit):
        if cc_bit == 0:
            return self.cpu.cc.get_overflow_bit()
        elif cc_bit == 1:
            return self.cpu.cc.get_underflow_bit()
        elif cc_bit == 2:
            return self.cpu.cc.get_divzero_bit()
        else:
            return self.cpu.cc.get_equalornot_bit()
    
    # TODO set cc bit value

