from typing_extensions import Self
from Registers.pc import pc
from Registers.instructionRegister import instructionregsiter
from memory import Memory 

class CU:
    def __init__(self):
         self.pc = pc('pc',12,0)
         self.ir = instructionregsiter('ixr',16,0)


mem_size = mem_size.get_memory_size(Self)