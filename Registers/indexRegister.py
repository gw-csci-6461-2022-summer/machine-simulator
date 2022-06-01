from atexit import register
from TemplateRegister import Register

#creating a indexRegister class for index register. indexRegisterclass is a child of TemplateRegister
class indexRegister(Register):
    def __init__(self,register_name,register_size,value, ixr_number):
        super().__init__('ixr',16,value)
        self.ixr_number = ixr_number

    def get_ixr_number(self):
        return self.ixr_number
        
# testing methods from super & child class - TO BE removed after
testixr= indexRegister('ixr',16,1,3)
# print(help(gpr)
print('The name:', testixr.get_register_name())
print('The size:', testixr.get_register_size())
print('The value:', testixr.get_value())
print('The value:', testixr.get_ixr_number())