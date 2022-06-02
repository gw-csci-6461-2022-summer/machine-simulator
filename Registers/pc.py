from TemplateRegister import Register

# creating a Pc class for progran counter register. Pc class is a child of TemplateRegister
# value is the address memory of the next instruction that will be executed 
class pc(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('pc',12,value)

    def increment_pc(self):
        self.value = (self.get_value() + 1)
        return self.value


