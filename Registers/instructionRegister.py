from TemplateRegister import Register
from mbr import mbr

# The fetched instruction is loaded into an instrcution register 
class instructionregsiter(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('ir',16,value)

    def get_instruction_from_mbr(self, mbr : mbr):
        self.value = mbr.value
    
    # ixr store instruction that needs to be read
    def get_instruction(self):
        return self.value