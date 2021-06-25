from board import *
import busio
import displayio
from adafruit_st7735r import ST7735R

displayio.release_displays()

spi = busio.SPI(clock=GP10, MOSI=GP11)
tft_cs = GP13
tft_dc = GP9

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=GP7
)

# display = ST7735R(display_bus, width=80, height=160)
display = ST7735R(
    display_bus, width=160, height=80, colstart=24, rotation=270, bgr=True
)
print("Hello World!")
