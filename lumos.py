from time import sleep

from camera_class import Camera

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x20

camera = Camera(CAMERA_ADDR, CAMERA_BUS)

#Test
for i in range(2):
    camera.SET_LED(3)
    sleep(1)
    camera.SET_LED(0)
    sleep(1)