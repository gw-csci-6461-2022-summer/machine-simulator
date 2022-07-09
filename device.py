class Device:

    def __init__(self):
        self.printer = 0
        self.keyboard = input('Please input to register\n')
        
    def get_keyboard(self):
        if self.keyboard == None:
            self.keyboard = 0
            return self.keyboard 
        else: 
            return self.keyboard
        
    def set_printer(self):
        self.printer = self.keyboard
        print(self.printer)

    def get_printer(self):
        return self.printer
