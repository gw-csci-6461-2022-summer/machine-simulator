import sys
sys.path.insert(0, './memory')
sys.path.insert(0, './Registers')
from Registers.indexRegister import indexRegister
from Registers.mar import mar
from instruction import Instruction
import helper_functions
from memory import Memory
from cpu import CPU

test_memory = Memory(2048)
test_memory.store_memory_value(31, 10)
test_cpu = CPU()
test_cpu.mbr.set_value(20)
print('value stored: ',test_memory.get_mem()[31])

inst = Instruction(test_cpu, test_memory)
inst.instruction_value = '0000101100011111'
inst.split_instruction()
opcode = inst.get_opcode()
index_gpr = inst.get_index_gpr()
print('opcode:',inst.get_opcode())
print('general purpose register:',inst.get_index_gpr())
print('index register:',inst.get_index_ixr())
print('indirect addressing:',inst.get_indirect_addressing())
print('address: ',inst.get_address())
print('converted opcode',int(opcode, base=2))
# print('testing decoding:',opcode.decoding_instruction())
ixr = indexRegister(register_name="IX1", register_size=16, value=2, ixr_number=helper_functions.binary_to_decimal(inst.get_index_ixr()))
mar_test = mar("mar", 12, 0)

inst.decoding_instruction()
inst.execute_store()
# inst1 = Instruction(test_cpu, test_memory)
# inst1.instruction_value = '0000101100011101'
# inst1.store()
