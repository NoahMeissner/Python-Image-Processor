# Noah Meissner 10.05.2024
from PIL import Image


"""
The implementation of a Kernel Processor.
This Processor will apply the Sharp and Blur Kernels to an input image.

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<kernel> : Kernel which was calculated by Sharpness.class and Blur.class

Output:
<image> : Image in the PIL Format
"""


class KernelProcessor:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end

    def process_filter(self, kernel):
        img = self.image.copy()
        width, height = img.size
        size = len(kernel)
        value = int((size - 1) / 2)
        bord_img = Image.new("RGB", (width + 2 * value, height + 2 * value))
        bord_img.paste(img, (value, value))

        for x in range(
                self.point_start[0] + value,
                self.point_end[0] + value):
            for y in range(
                    self.point_start[1] + value,
                    self.point_end[1] + value):
                pixel_sum = [0, 0, 0]
                for i in range(size):
                    for j in range(size):
                        pixel = (bord_img
                                 .getpixel((x + i - value, y + j - value)))
                        pixel_sum[0] += pixel[0] * kernel[i][j]
                        pixel_sum[1] += pixel[1] * kernel[i][j]
                        pixel_sum[2] += pixel[2] * kernel[i][j]
                new_pixel = tuple(int(channel) for channel in pixel_sum)
                img.putpixel((x - value, y - value), new_pixel)

        return img
