from TemplateRegister import Register
from pc import pc
from mar import mar
from gpr import gpr 
from indexRegister import indexRegister

# testing gpr 
testgpr= gpr('gpr',16,1,3)
print('The name:', testgpr.get_register_name())
print('The size:', testgpr.get_register_size())
print('The value:', testgpr.get_value())
print('The gpr number:', testgpr.get_gpr_number())

# testing ixr
testixr= indexRegister('ixr',16,1,2)
print('The name:', testixr.get_register_name())
print('The size:', testixr.get_register_size())
print('The value:', testixr.get_value())
print('The ixr number:', testixr.get_ixr_number())

# testing pc 
testpc = pc('pc',12,1)
print('The name:', testpc .get_register_name())
print('The size:', testpc .get_register_size())
print('The value:', testpc .get_value())
incremented_pc = testpc.increment_pc()
print('The incremented value:', testpc .get_value())

# testing mar 
testmar = mar('mar',12,5)
print('The name:', testmar.get_register_name())
print('The size:', testmar.get_register_size())
print('The value:', testmar .get_value())
testmar.get_pc_value(testpc)
print('The value from pc :', testmar.get_pc_value(testpc))

