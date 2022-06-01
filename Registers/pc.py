from TemplateRegister import Register

#creating a Pc class for progran counter register. Pc class is a child of TemplateRegister
class pc(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('pc',12,value)

    def increment_pc(self):
        latest_pc_value = (self.get_value() + 1)
        return latest_pc_value
    
 

# testing - TO BE removed after
testpc = pc('pc',16,1)
print('The name:', testpc.get_register_name())
print('The size:', testpc.get_register_size())
print('The value:', testpc.get_value())
print('The value:', testpc.increment_pc())


