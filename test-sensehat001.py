from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = 255
g = (0,255,0)
#b = (0,0,0)
y = (r,255,0)

sense.clear()
# Set up where each colour will display
# Define some colours
B = (102, 51, 0)
b = (0, 0, 255)
S = (205,133,63)
W = (255, 255, 255)

# Set up where each colour will display
steve_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]
sense.set_rotation(180)

# Display these colours on the LED matrix
sense.set_pixels(steve_pixels)

sleep(2)

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()
while True:
    sense.show_message("Hola -->", text_colour= y, back_colour = b)

