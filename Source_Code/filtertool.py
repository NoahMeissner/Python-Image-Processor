from PIL import Image
from Filter.Contrast import Contrast
from Filter.Brightness import Brightness
from Filter.Threshold import Threshold
from Filter.Blur import Blur
from Filter.Sharpness import Sharpness
from Filter.Erode import Erode
from Filter.Dilate import Dilate
from Filter.Swirl import Swirl
from graphical_interface import GraphicalInterface
import click


@click.command()
@click.option('--filter_type',
              default=None,
              help='''
              Available Filters:
              Threshold
              Brightness
              Contrast
              Blur
              Sharpness
              Erode
              Dilate
              Swirl
              ''')
@click.option('--value',
              default=None,
              prompt='A value to filter on',
              help='''
              Each Filter has a specific range of values
              (for more information pick the Graphical User Interface)
              ''')
@click.option('--area',
              default=None,
              help='''
              Set an area to filter on in the
              format: x_min,y_min,x_max,y_max
              ''')
@click.option('--original_image',
              default=None,
              prompt='Image to Process on',
              help='Image where filters are applied')
def set_filter(original_image, filter_type, value, area):
    if original_image is None:
        print("No image provided.")
        return

    img = Image.open(original_image)
    value = int(value)

    # Check if the area has been specified and extract the coordinates
    if area:
        x_min, y_min, x_max, y_max = map(int, area.split(','))
        point_start = (x_min, y_min)
        point_end = (x_max, y_max)
    else:
        point_start = point_end = None

    # Initialise filter object
    filter_object = None
    match filter_type:
        case "threshold":
            filter_object = Threshold(img, point_start, point_end)
        case "brightness":
            filter_object = Brightness(img, point_start, point_end)
        case "contrast":
            filter_object = Contrast(img, point_start, point_end)
        case "sharp":
            filter_object = Sharpness(img, point_start, point_end)
        case "blur":
            filter_object = Blur(img, point_start, point_end)
        case "erode":
            filter_object = Erode(img, point_start, point_end)
        case "dilate":
            filter_object = Dilate(img, point_start, point_end)
        case "swirl":
            filter_object = Swirl(img, point_start, point_end)
        case _:
            print("Unknown Filter")

    filter_range = filter_object.get_slider_information()
    if filter_range[0] <= value <= filter_range[1]:
        final_image = filter_object.process(value)
        show_image(final_image)
    else:
        print("Value out of range")


def show_image(filtered_image):
    GraphicalInterface(filtered_image)


if __name__ == '__main__':
    set_filter()
