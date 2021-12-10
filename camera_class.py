import smbus

class Camera():
    def __init__(self, address, camera_bus):
        self.addr = address    
        self.bus = smbus.SMBus(camera_bus)

        #self.__setup__()

    def write(self, register ,command):
        self.bus.write_byte_data(self.addr, register, command)

    def read(self, register):
        return self.bus.read_byte_data(self.addr, register)
    
    def read_range(self, start, end):
        results = []

        for i in range(start, end):
            data = self.read(i)
            results.append("REG : {}, DATA : {}".format(hex(i), hex(data)))

        return results
    
    def SET_LED(self, led_state):
        
        if led_state == False: self.write(0x02, 0x20)
        elif led_state == True: self.write(0x02, 0xFF)

    def __setup__(self):
            self.write(0x06, 0x00)
            self.write(0x02, 0x20)