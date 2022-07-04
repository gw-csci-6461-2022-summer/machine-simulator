from TemplateRegister import Register

#creating a cc class for condition code register. cc class is a child of TemplateRegister
class cc(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('cc',4,value)
