from os import sleep

from camera_class import Camera

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x20

camera = Camera(CAMERA_ADDR, CAMERA_BUS)

#Test
camera.SET_LED(1, True)

sleep(10)

camera.SET_LED(1, False)
camera.SET_LED(2, True)

sleep(10)

camera.SET_LED(2, False)