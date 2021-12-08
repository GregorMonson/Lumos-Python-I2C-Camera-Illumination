from camera_class import Camera

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x00

camera = Camera(CAMERA_ADDR, CAMERA_BUS)