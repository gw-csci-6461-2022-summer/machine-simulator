from TemplateRegister import Register

#creating mbr class for memory buffer register. mbr is a child of TemplateRegister
class mbr(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('mbr',16,value)

# inherits methods from TemplateRegister. For example: set_value