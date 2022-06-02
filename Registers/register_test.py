from TemplateRegister import Register
from indexRegister import indexRegister
from pc import pc
from mar import mar
from gpr import gpr 
from mbr import mbr 
from mfr import mfr

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

# testing mbr 
testmbr = mbr('mbr',4,10)
print('The name:', testmbr.get_register_name())
print('The size:', testmbr.get_register_size())
print('The value:', testmbr .get_value())

# testing mfr 
testmfr = mfr('mfr',4,12)
print('The name:', testmfr.get_register_name())
print('The size:', testmfr.get_register_size())
print('The value:', testmfr.get_value())

