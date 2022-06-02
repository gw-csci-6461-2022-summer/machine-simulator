from TemplateRegister import Register

class ALU:
  def __init__(self, cc):
    self.irr = Register("register", 16, '0'*16)
    self.value = 0
    self.cc = cc

  def reset(self):
    self.irr = Register("register", 16, '0'*16)
    self.value = 0
  
  def arithmetic_cal(self, operation: str, o1: str, o2: str):
    self.irr.reset()
    self.value = 0
    o1_value = int(o1, 2)
    o2_value = int(o2, 2)
    if operation == '+':
        self.value = o1_value + o2_value
    elif operation == '-':
        self.value = o1_value - o2_value
    elif operation == '*':
        self.irr.size = 32
        self.value = o1_value * o2_value
    elif operation == '/':
        self.value = int(o1_value / o2_value)
    elif operation == '%':
        self.value = o1_value % o2_value
    return self.irr.value
    
    
    # def __init__(self):
    #     self.alu_ops = {
    #         'ADD': lambda a, b: round(a + b, 2),  #Add
    #         'SUB': lambda a, b: round(b - a, 2),  #Subtract
    #         'DIV': lambda a, b: round(b / a, 2),  #Divide
    #         'MUL': lambda a, b: round(a * b, 2),  #Multiply
    #         'AND': lambda a, b: a & b,            #Bitwise and
    #         'OR' : lambda a, b: a | b,            #Bitwise or
    #         'XOR': lambda a, b: a ^ b,            #Bitwise xor
    #         'NOT': lambda a: ~a,                  #Bitwise not
    #     }

    # def operateOnReg(self, op, op1, op2, reg):
    #     if op in self.alu_ops:
    #       Register.set_value(reg, self.alu_ops[op](op1, op2))
    #       return reg
          
        