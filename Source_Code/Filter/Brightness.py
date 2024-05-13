# Noah Meissner 10.05.2024

"""
The implementation of a Brightness filter

Theories
- Source: Previous Lecture Tasks

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


class Brightness:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, factor):
        img = self.image.copy()
        for x in range(self.point_start[0], self.point_end[0]):
            for y in range(self.point_start[1], self.point_end[1]):
                pixel = img.getpixel((x, y))
                if isinstance(pixel, tuple):
                    pixel_new = tuple(int(a * factor) for a in pixel)
                    img.putpixel((x, y), pixel_new)
                else:
                    pixel_new = int(pixel * factor)
                    img.putpixel((x, y), pixel_new)

        return img

    @staticmethod
    def get_slider_information():
        return [0, 10]
