
class CPU:
    process=None
    core=None

    def __init__(self,process,core):
        self.process = process
        self.core = core

    def __str__(self):
        return f"{self.core} x {self.process}" 

class Power:
     input_power = None
     output_power = None
      
     def __init__ (self,input_power,output_power):
         self.input_power = input_power
         self.output_power = output_power
     def __str__(self):
         return f"input_power is {self.input_power} x  output_power is {self.output_power}" 
class PC (CPU,Power):
    def __init__(self, process, core,input_power,output_power):
        super().__init__(process, core)
        Power.__init__(self,input_power,output_power)


    def get_PC_config(self):

     print(f"cpu is {self.process} x {self.core} ,power is {self.input_power} x {self.output_power} ")

diy_pc = PC(20,10,"220v","12v")

diy_pc.get_PC_config()