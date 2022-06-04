from instruction import Instruction

inst = Instruction()
inst.instruction_value = '0000011101100101'
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
inst.decoding_instruction()