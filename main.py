import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    # do the rest...
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    # the value range from 0 to 65535
    # try to divide this into len(led_pins)
    volume = microphone.value
    
    MAX_VAL_CEIL = 65535
    
    jump_step = MAX_VAL_CEIL // len(led_pins)

    print(volume)
    
    leds_height = volume // jump_step
    
    
    # first we turn all off
    for x in range(0, len(led_pins)):
        leds[x].value = 0
    
    # then turn on the leds that are in range
    for x in range(0, leds_height):
        leds[x].value = 1

    

    # sleep(1)
