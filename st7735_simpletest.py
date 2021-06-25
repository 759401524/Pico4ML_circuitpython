# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio
and draw a solid red background
"""
import time
import board
import busio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
from adafruit_displayio_layout.layouts.grid_layout import GridLayout

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
tft_cs = board.GP13
tft_dc = board.GP9

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.GP7
)

# display = ST7735R(display_bus, width=80, height=160)
display = ST7735R(
    display_bus, width=160, height=80, colstart=24, rotation=270, bgr=True
)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)
time.sleep(1)

# Make a background color fill
color_bitmap = displayio.Bitmap(160, 80, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
time.sleep(1)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(150, 70, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)
time.sleep(1)

# Draw a label
text_group = displayio.Group(max_size=10, scale=2, x=11, y=40)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
time.sleep(1)

splash.append(Line(20, 30, 70, 10, 0xFF0000))
splash.append(Line(70, 10, 20, 10, 0xFF0000))
splash.append(Line(20, 10, 70, 30, 0xFF0000))
splash.append(Line(70, 30, 20, 30, 0xFF0000))
time.sleep(1)

text = " Color Background Hello world"
text_area = label.Label(
    terminalio.FONT, text=text, color=0x0000FF, background_color=0xFFAA00
)
text_area.x = 10
text_area.y = 10

print("background color is {:06x}".format(text_area.background_color))

display.show(text_area)
time.sleep(1)
text_area.background_color = 0xFF0000
print("background color is {:06x}".format(text_area.background_color))
time.sleep(1)
text_area.background_color = None
print("background color is {}".format(text_area.background_color))
time.sleep(1)

while True:
    pass
