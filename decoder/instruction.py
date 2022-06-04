'''steps for decoding an instruction 
1 - create an object instruction 
2 - read instruction from instruction register
3-  use setters to set the values that are read in object instruction 
4 - use getters the read value form object instruction '''

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
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.opcode
    
    def get_index_gpr(self):
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.index_gpr
    
    def get_index_ixr(self):
        self.opcode,index_gpr,index_ixr,indirect_addressing,address = self.split_instruction()
        return self.index_ixr
    
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
        elif self.opcode == 1:
            print ('Instruction: LDR')
            # TODO: execute_load()
        elif self.opcode == 2:
            print ('Instruction: STR')
            # TODO: execute_store()

    def fetching(self):
        # TODO:
        return None
    
    def execute_halt():
        # TODO:
        return None

    def execute_store():
        # TODO:
        return None



    

