import smbus

class Camera():
    def __init__(self, address, camera_bus):
        self.addr = address    
        self.bus = smbus.SMBus(camera_bus)

    def write(self, register ,command):
        self.bus.write_byte_data(self.addr, register, command)

    def read(self, register):
        self.bus.read_byte_data(self.addr, register)