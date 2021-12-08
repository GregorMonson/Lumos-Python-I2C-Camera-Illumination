import smbus

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x00

class Camera():
    def __init__(self, address, camera_bus):
        self.addr = address    
        self.bus = smbus.SMBus(camera_bus)

    def write(self, register ,command):
        self.bus.write_byte_data(self.addr, register, command)

    def read(self, register):
        self.bus.read_byte_data(self.addr, register)

camera = Camera(CAMERA_ADDR, CAMERA_BUS)

camera.write(0x00, 0x01)

