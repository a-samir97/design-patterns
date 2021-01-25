class Computer:
    
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = "Serial number : %s\n Memory: %s\n HDD: %s\n GPU: %s" % (self.serial, self.memory, self.hdd, self.gpu)
        return info


class ComputerBuilder:
    
    def __init__(self, serial_number):
        self.computer = Computer(serial_number)
    
    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount
    
    def configure_gpu(self, amount):
        self.computer.gpu = amount


class HardwareEngineer:

    def __init__(self):
        self.computer_builder = None
    
    def construct_computer(self, serial, memory, hdd, gpu):
        self.computer_builder = ComputerBuilder(serial)
        steps = (self.computer_builder.configure_memory(memory),
                 self.computer_builder.configure_hdd(hdd),
                 self.computer_builder.configure_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.computer_builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(serial=123,
                                hdd=500, 
                                memory=8, 
                                gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)

if __name__ == '__main__':
    main()


    
