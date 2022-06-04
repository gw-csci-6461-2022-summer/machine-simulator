# from cgi import test
from control_unit import ControlUnit

# creating a Pc class for progran counter register. Pc class is a child of TemplateRegister
# value is the address memory of the next instruction that will be executed 
class pc(ControlUnit):
    def __init__(self, test_file):
        super().__init__(test_file)
        self.value = None
        
    def increment_pc(self):
        if self.value == None:
            self.value = 0
        else:
            self.value = self.value + 1
