# Noah Meissner 10.05.2024
import math
from PIL import Image

"""
The implementation of a Swirl filter.

Theories
- Source :
https://geekofficedog.blogspot.com/2013/04/hello-swirl-swirl-effect-tutorial-in.html
- Source :
https://eeweb.engineering.nyu.edu/~yao/EL5123/lecture12_ImageWarping.pdf

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


class Swirl:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, rotation):
        width, height = self.image.size
        rotation = - rotation * math.pi / 180  # Grad -> Radiant
        x_rotation_point = int((self.point_start[0] + self.point_end[0]) / 2)
        y_rotation_point = int((self.point_start[1] + self.point_end[1]) / 2)
        img = Image.new('RGB', (width, height), "black")

        for x in range(self.point_start[0], self.point_end[0]):
            for y in range(self.point_start[1], self.point_end[1]):
                pixel = self.image.getpixel((x, y))
                angle = ((x - x_rotation_point) ** 2
                         + (y - y_rotation_point) ** 2) ** 0.5
                rotation_angle = math.pi * (angle * rotation) / 512
                x_new = int((x - x_rotation_point) * math.cos(rotation_angle)
                            + (y - y_rotation_point) * math.sin(
                    rotation_angle) + x_rotation_point)
                y_new = int(-(x - x_rotation_point) * math.sin(rotation_angle)
                            + (y - y_rotation_point) * math.cos(
                    rotation_angle) + y_rotation_point)

                if self.point_start[0] <= x_new < self.point_end[0]:
                    if self.point_start[1] <= y_new < self.point_end[1]:
                        img.putpixel((x_new, y_new), pixel)
        return img

    @staticmethod
    def get_slider_information():
        return [0, 360]
