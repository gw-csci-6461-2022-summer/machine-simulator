# machine-simulator
csci 6461 computer system architecture project (phase I & II) 

## Testing Transfer Instructions
* start the gui
```
python3 .\gui_grid.py
```
* click the init button and select the test_transfer_instruction.txt file
* click the ss button to step through the program

### Test JZ
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0001 2A07 | OpCode: JZ (jump if zero), PC=1, GPR2=11783, PC=2 

### Test JNE
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0002 2E07 | OpCode: JNE (jump if not equal) PC=2, GPR2=0, EA->PC=111 

### Test JCC
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0003 3207 | OpCode: JCC (jump if condition code) PC=  

### Test JMA
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)   
0004 3607 | OpCode: JMA (unconditional jump to address) PC =
0005 3A07 | OpCode: JSR (jump and save return address)
0006 3E07 | OpCode: RFS (return from subroutine)
0007 4207 | OpCode: SOB (subtract one and branch)
0008 4607 | OpCode: JGE (jump greater than or equal to)

### Test JSR
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0005 3A07 | OpCode: JSR (jump and save return address)

### Test RFS
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0006 3E07 | OpCode: RFS (return from subroutine)

### Test SOB
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0007 4207 | OpCode: SOB (subtract one and branch)

### Test JGE
Memory Location (hexadecimal) \& Instruction (hexadecimal) | Execution Explanation
--------- | ------
0000 0607 | Load (LDR)  
0008 4607 | OpCode: JGE (jump greater than or equal to)