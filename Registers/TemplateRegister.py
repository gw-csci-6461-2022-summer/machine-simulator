# defining super class register 
class Register:
    
    # defining __init__() function to assign values to object properties 
    def __init__(self,register_name,register_size,value):
        self.register_size = register_size
        self.register_name= register_name
        self.value = value

    # getters to access register attribute 
    def get_register_size(self):
        return self.register_size

    def get_register_name(self):
        return self.register_name

    def get_value(self):
        return self.value

    # setters to assign values to register attribute 
    def set_register_size(self,register_number):
        self.register_number = register_number

    def set_register_name(self, register_name):
        self.register_name = register_name

    def set_value(self,value):
        self.value = value 

