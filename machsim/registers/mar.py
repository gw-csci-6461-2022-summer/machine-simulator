from pc import pc

# mar holds the address of the next location in memory to be accessed. This value will be obtained from the program counter.
class mar(pc):
    def __init_(self,test_file):
        super().__init__(test_file)

    def get_pc_value(self):   
        self.increment_pc()
        ram_mem = self.hold_value
        loaded_value = self.hold_value[self.value]
        if self.value < len(ram_mem):
            with open("mar_holder.txt", "w") as f:
                f.write(str(loaded_value[0]))
            return loaded_value[0]
        else:
            print("Process Complete.")

       
    def convert_to_binary(self):
        vale = self.get_pc_value()
        return "{0:b}".format(vale)



