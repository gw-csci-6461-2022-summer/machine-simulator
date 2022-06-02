from TemplateRegister import Register

#creating indexRegister class for index register. indexRegisterclass is a child of TemplateRegister
class indexRegister(Register):
    def __init__(self,register_name,register_size,value, ixr_number):
        super().__init__('ixr',16,value)
        self.ixr_number = ixr_number

    def get_ixr_number(self):
        return self.ixr_number
        