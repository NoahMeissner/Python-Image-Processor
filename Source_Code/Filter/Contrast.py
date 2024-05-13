# Noah Meissner 10.05.2024


"""
The implementation of a Contrast filter

Input:
<image> : Image in the PIL Format
<point_start> : Start point of the image to apply filter
<point_end> : End point of the image to apply filter
<value> : value how strong filter should be applied

Output:
<image> : Image in the PIL Format
"""


def over(value, middle, factor):
    return int((value - middle) * factor + middle)


def under(value, factor, left):
    return int(left + value * factor)


class Contrast:

    def __init__(self, image, point_start, point_end):
        self.image = image
        self.point_start = point_start
        self.point_end = point_end
        if point_start is None or point_end is None:
            width, height = self.image.size
            self.point_start = [0, 0]
            self.point_end = [width, height]

    def process(self, factor):
        image = self.image.copy().convert('RGB')

        min_pixel_intensity = [255, 255, 255]
        max_pixel_intensity = [0, 0, 0]

        for x in range(self.point_start[0], self.point_end[0]):
            for y in range(self.point_start[1], self.point_end[1]):
                r, g, b = image.getpixel((x, y))
                for i, v in enumerate([r, g, b]):
                    min_pixel_intensity[i] = min(min_pixel_intensity[i], v)
                    max_pixel_intensity[i] = max(max_pixel_intensity[i], v)
        middle = [(max_pixel_intensity[i] + min_pixel_intensity[i]) / 2
                  for i in range(3)]
        left = [middle[i] - ((middle[i] - min_pixel_intensity[i]) * factor)
                for i in range(3)]

        for x in range(self.point_start[0], self.point_end[0]):
            for y in range(self.point_start[1], self.point_end[1]):
                pixel = image.getpixel((x, y))
                new_pixel = []
                for i in range(3):
                    if pixel[i] > middle[i]:
                        new_pixel.append(over(pixel[i], middle[i], factor))
                    else:
                        new_pixel.append(under(pixel[i], factor, left[i]))
                image.putpixel((x, y), tuple(new_pixel))

        return image

    @staticmethod
    def get_slider_information():
        return [0, 20]
