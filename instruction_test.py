import sys
sys.path.insert(0, './memory')
sys.path.insert(0, './Registers')
from Registers.indexRegister import indexRegister
from Registers.mar import mar
from instruction import Instruction
import helper_functions

inst = Instruction()
inst.instruction_value = '0000011100011111'
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
# print('testing decoding:',opcode.decoding_instruction())
ixr = indexRegister(register_name="IX1", register_size=16, value=2, ixr_number=helper_functions.binary_to_decimal(inst.get_index_ixr()))
mar_test = mar("mar", 12, 0)
inst.decoding_instruction()
inst.load(ixr, mar_test)
