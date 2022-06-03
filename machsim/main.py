def main():
   
   # make instance of CPU
    cpu = CPU()
    def UploadFile(event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
        
        # TODO : here we call functions to parse the file and init the machine
        CPU.load_program(cpu, filename)

    # make instance of GUI


