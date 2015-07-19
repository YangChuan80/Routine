class Computer:
    def __init__(self, cpu_frequency):
        self.cpu=cpu_frequency
     
class Notebook(Computer):
    def __init__(self, cpu_frequency, memory_size):
        self.memory=memory_size
        Computer.__init__(self, cpu_frequency)

       
class Laptop(Computer):
    def __init__(self, cpu_frequency, memory_size):
        self.memory=memory_size
        super().__init__(cpu_frequency)

asus=Notebook(1.1, 1000)
alien=Laptop(2.6, 2000)