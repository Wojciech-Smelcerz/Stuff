# IMPORT
from PIL import Image
import colorsys
import math

# FUNCTIONS
# color
def color(iterations: int):
    # return (int(iterations%8*32), int(iterations%16*16), int(iterations%32*8))
    return (int(iterations*1), int(iterations*2), int(iterations*3))
# mandelbrot
def mandelbrot(x: float, y: float, iterations: int):
    c = complex(x, y)
    z = 0
    for i in range(iterations):
        if abs(z) > 2:
            return color(iterations=i)
        z = z**2 + c
    # return 0
    return (255, 255, 255)
# plot
def plot(image: Image.Image, position: tuple[float, float], zoom: float, iterations: int):
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel(
                xy=(x, y),
                value=mandelbrot(
                    x=x/(image.width*zoom) - 0.5/zoom + position[0],
                    y=y/(image.height*zoom) - 0.5/zoom + position[1],
                    iterations=iterations))
