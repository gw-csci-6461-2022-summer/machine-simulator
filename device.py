class Device:

    def __init__(self):
        self.printer = 0
        self.keyboard = input('Please input to register\n')

    def set_keyboard(self, val):
        self.keyboard.append(val)

    def get_keyboard(self):
        if self.keyboard == None:
            self.keyboard = 0
            return self.keyboard 
        else: 
            return self.keyboard
        

    def set_printer(self, val):
        self.printer = val

    def get_printer(self):
        return self.printer
