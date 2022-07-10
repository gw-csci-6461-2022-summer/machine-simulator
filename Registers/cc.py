from TemplateRegister import Register
from helper_functions import decimal_to_bit_array_unsigned
from helper_functions import binary_to_decimal


#creating a cc class for condition code register. cc class is a child of TemplateRegister
class cc(Register):
    def __init__(self,register_name,register_size,value):
        super().__init__('cc',4,value)

    # get condition codes
    def get_overflow_bit(self):
        return int(decimal_to_bit_array_unsigned(self.value,self.register_size)[0])

    def get_underflow_bit(self):
        return int(decimal_to_bit_array_unsigned(self.value,self.register_size)[1])

    def get_divzero_bit(self):
        return int(decimal_to_bit_array_unsigned(self.value,self.register_size)[2])

    def get_equalornot_bit(self):
        return int(decimal_to_bit_array_unsigned(self.value,self.register_size)[3])

    # toggle condition codes
    def toggle_overflow_bit(self):
        bit_array = decimal_to_bit_array_unsigned(self.value,self.register_size)
        toggled_bit = str((int(bit_array[0])+1)%2)
        bit_array = bit_array[:0] + toggled_bit + bit_array[0+1:] 
        self.value = binary_to_decimal(int(bit_array))
        return 

    def set_underflow_bit(self,bit_value):
        self.value = 0
        return 

    def set_divzero_bit(self):
        self.value = 0
        return

    def set_equalornot_bit(self):
        self.value = 0
        return

