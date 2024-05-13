# Noah Meissner 10.05.2024


"""
The implementation of a Dilation filter

Theories
- Source : https://homepages.inf.ed.ac.uk/rbf/HIPR2/dilate.htm#1

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


class Dilate:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, kernel_size):
        kernel_size = int(kernel_size)
        image = self.image.convert('L').copy()
        img = self.image.convert('L').copy()

        for x in range(
                self.point_start[0] + kernel_size,
                self.point_end[0] - kernel_size):
            for y in range(
                    self.point_start[1] + kernel_size,
                    self.point_end[1] - kernel_size):
                min_pixel = 0
                for i in range(-kernel_size, kernel_size + 1):
                    for j in range(-kernel_size, kernel_size + 1):
                        if i == 0 or j == 0:
                            neighbor_pixel = image.getpixel((x + i, y + j))
                            min_pixel = max(min_pixel, neighbor_pixel)

                img.putpixel((x, y), min_pixel)

        return img

    @staticmethod
    def get_slider_information():
        return [0, 10]
