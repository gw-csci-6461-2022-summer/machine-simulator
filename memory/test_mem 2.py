from memory import Memory

# testing mem functions 
test_memory = Memory(20)

print("memory size: " + str(test_memory.get_memory_size()))
print("mem value: " + str(test_memory.get_memory_value(8))) # should be 0

# insert values into memory then do a few gets
test_memory.store_memory_value(9, 124)
test_memory.store_memory_value(20, 9348)
test_memory.store_memory_value(0, 876)

print("mem value @ location 0: " + str(test_memory.get_memory_value(0))) # should be 876
print("mem value @ location 9: " + str(test_memory.get_memory_value(9))) # should be 124
print("mem value @ location 20: " + str(test_memory.get_memory_value(20))) # should be 9348

print("mem value @ location 1: " + str(test_memory.get_memory_value(1))) # should be 0
print("mem value @ location 2: " + str(test_memory.get_memory_value(2))) # should be 0
print("mem value @ location 19: " + str(test_memory.get_memory_value(19))) # should be 0

# reset and check 
test_memory.reset_memory()

print("mem value @ location 0: " + str(test_memory.get_memory_value(0))) # should be 0
print("mem value @ location 9: " + str(test_memory.get_memory_value(0))) # should be 0
print("mem value @ location 20: " + str(test_memory.get_memory_value(0))) # should be 0