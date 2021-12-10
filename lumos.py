from time import sleep

from camera_class import Camera

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x20

camera = Camera(CAMERA_ADDR, CAMERA_BUS)

#Test
camera.SET_LED(3)
sleep(20)
camera.SET_LED(0)