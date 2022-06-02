from TemplateRegister import Register
from pc import pc

# mar holds the address of the next location in memory to be accessed. This value will be obtained from the program counter.
class mar(Register):
    def __init_(self,register_name,register_size,value):
        super().__init__('mar',12,value)


    def get_pc_value(self,incremented_pc : pc):
        self.set_value(incremented_pc.get_value())

       





