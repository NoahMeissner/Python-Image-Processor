# Noah Meissner 10.05.2024
from Filter.KernelProcessor import KernelProcessor

"""
The implementation of a Sharp filter.

Theories
- Source : https://d-nb.info/1225683793/34

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


def sharp_kernel(value):
    kernel_size = 2 * value + 1
    kernel = [[-1 / (kernel_size ** 2) for _ in range(kernel_size)]
              for _ in range(kernel_size)]
    kernel[value][value] = 1 + (kernel_size ** 2 - 1) / (kernel_size ** 2)
    return kernel


class Sharpness:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, value):
        value = int(value)
        kernel = sharp_kernel(value)
        processor = KernelProcessor(
            self.image,
            self.point_start,
            self.point_end)
        return processor.process_filter(kernel)

    @staticmethod
    def get_slider_information():
        return [0, 10]
