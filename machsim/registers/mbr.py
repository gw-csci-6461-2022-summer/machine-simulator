from TemplateRegister import Register

#creating mbr class for memory buffer register. mdr is a child of TemplateRegister
class mbr(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('mbr',16,value)

    # TO DO
    def get_value_from_mempry(self,memory_value):
        return memory_value

    # TO DO 
    def set_value_in_mempry(self,memory_value):
        return memory_value