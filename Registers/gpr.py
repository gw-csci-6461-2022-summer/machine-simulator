from TemplateRegister import Register

#creating a gpr class for general pupose register. gpr class is a child of TemplateRegister
class gpr(Register):
    def __init__(self,register_name,register_size,value,gpr_number):
        super().__init__('gpr',16,value)
        self.gpr_number = gpr_number

    def get_gpr_number(self):
        return self.gpr_number
        

# testing - TO BE removed after
testgpr= gpr('gpr',16,1,3)
# print(help(gpr))
print('The name:', testgpr.get_register_name())
print('The size:', testgpr.get_register_size())
print('The value:', testgpr.get_value())
print('The value:', testgpr.get_gpr_number())






    