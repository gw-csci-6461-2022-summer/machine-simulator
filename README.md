# csci 6461 computer system architecture machine simulator

# Executable
make executable 
```
py setup.py py2exe
```
run executable
```
.\dist\machine-simulator.exe
```

# Design

## Arithmatic Logic Unit (ALU)
arithmetic_unit  
logic_unit  

add_value()  
sub_value()  
add_imm()  
sub_imm()  

## Assembler
value  

convert_to_binary(String)  
get_value():value  
set_value(value)  

## Central Processing Unit (CPU)
Memory  
PC  
CC  
MAR  
MDR  
MFR  
GPR  
IR  
IXR  

CPU()  
init_cpu()  
read_instruction(String instruction)  
validate_instuction(String instruction)  
execute_inctruction()  
load()   
store()   
step()  

## Memory
words: int [ ]  
size

Memory()  
get_memory_size()  
get_memory_value()  
store_memory_value()  
reset_memory()
