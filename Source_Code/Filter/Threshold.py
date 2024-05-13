# Noah Meissner 10.05.2024

"""
The implementation of a Threshold filter.

Theories
- Source : Previous Lecture Task

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


class Threshold:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, value):
        point_start_x = self.point_start[0]
        point_start_y = self.point_start[1]
        point_end_x = self.point_end[0]
        point_end_y = self.point_end[1]
        img = self.image.copy().convert('L')
        for x in range(point_start_x, point_end_x):
            for y in range(point_start_y, point_end_y):
                if img.getpixel((x, y)) < value:
                    new_value = 0
                else:
                    new_value = 255
                img.putpixel((x, y), new_value)
        return img

    @staticmethod
    def get_slider_information():
        return [0, 255]
