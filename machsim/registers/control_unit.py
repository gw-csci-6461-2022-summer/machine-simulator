from cgi import test
from helper_functions import hex_to_decimal as hx_dc 

class ControlUnit:
    def __init__(self, test_file):
       self.test_file = open(test_file, "r").readlines()
       self.ram_mem()

#Split inputs [0]X [1]Y 
    def ram_mem(self):
        self.hold_value = {}
        for i,x in enumerate(self.test_file): 
            x = x.split()
            self.hold_value[i] = [hx_dc(x[0]), hx_dc(x[1])]
        
