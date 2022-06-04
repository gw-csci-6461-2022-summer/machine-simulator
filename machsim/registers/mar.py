from pc import pc

# mar holds the address of the next location in memory to be accessed. This value will be obtained from the program counter.
class mar(pc):
    def __init_(test_file):
        super().__init__(test_file)

    def get_pc_value(self):   
        self.increment_pc()
        if self.value < len(self.hold_value):
            with open("mar_holder.txt", "w") as f:
                f.write(str(self.hold_value[self.value][1]))
            return self.hold_value[self.value][1]
        else:
            print("Process Complete.")

       





