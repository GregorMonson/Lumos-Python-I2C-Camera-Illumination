from time import sleep

from camera_class import Camera

#Camera bus id
CAMERA_BUS = 1
#Camera I2C address
CAMERA_ADDR = 0x20

camera = Camera(CAMERA_ADDR, CAMERA_BUS)

print("This is a simple script written by Gregor Monson to toggle Camera LED state.")
print("For assistance contact gregor.monson@lumiradx.com")
print("To exit press Ctrl + c, enjoy!")

#On off Script
while True:
    raw_input("Press Enter to Turn ON LED's\n")
    camera.SET_LED(True)
    raw_input("Press Enter to Turn OFF LED's\n")
    camera.SET_LED(False)