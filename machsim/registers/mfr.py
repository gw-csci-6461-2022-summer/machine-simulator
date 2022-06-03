from TemplateRegister import Register

#creating mfr class for memory fault register. mfr is a child of TemplateRegister
class mfr(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('mfr',4,value)
