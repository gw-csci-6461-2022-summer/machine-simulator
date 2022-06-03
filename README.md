# Machine Simulator

## Executable
make executable 
```
py setup.py py2exe
```
run executable
```
.\dist\machine-simulator.exe
```

## machsim package structure

```python
machsim/
  __init__.py
  cpu.py
    - class CPU:
  gui.py
    - class ???:
  helper_functions.py
    - def hex_to_decimal(value)
    - def print_memory_contents(Memory)
    - def decimal_to_bit_array_unsigned(value, size)
    - def decimal_to_bit_array_signed(value, size)
    - def binary_to_decimal(value)
  main.py
    - def main()
  memory/
    __init__.py
    memory.py
      - def __init__(self, size)
      - def get_memory_size(self)
      - def get_memory_value(self, word)
      - def store_memory_value(self, word, value)
      - def reset_memory(self)
    test_mem.py
  registers/
    __init__.py
    ALU.py
      - class ALU:
    gpr.py
      - class gpr(Register):
    indexRegister.py
      - class indexRegister(Register):
    instructionRegister.py
      - class instructionregsiter(Register):
    mar.py
      - class mar(Register):
    mbr.py
      - class mbr(Register):
    mfr.py
      - class mfr(Register):
    pc.py
      - class pc(Register):
    register_test.py
    TemplateRegister.py
      - class Register:
```