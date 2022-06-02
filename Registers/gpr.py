from TemplateRegister import Register

#creating a gpr class for general pupose register. gpr class is a child of TemplateRegister
class gpr(Register):
    def __init__(self,register_name,register_size,value,gpr_number):
        super().__init__('gpr',16,value)
        self.gpr_number = gpr_number

    def get_gpr_number(self):
        return self.gpr_number



    