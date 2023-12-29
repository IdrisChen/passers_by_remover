"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    p_b = pixel.blue
    p_r = pixel.red
    p_g = pixel.green
    red_pow = (red-p_r)**2
    blue_pow = (blue-p_b)**2
    green_pow = (green-p_g)**2
    color_distance = math.sqrt(red_pow+blue_pow+green_pow)
    return color_distance

def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    c_list = [0, 0, 0]
    for i in range(len(pixels)):
        c_list[0] += pixels[i].red
        c_list[1] += pixels[i].green
        c_list[2] += pixels[i].blue
    #avg_list = c_list(ele/len(pixels) for ele in c_list)
    for i in range(len(c_list)):
        c_list[i] = c_list[i]/len(pixels)
        c_list[i] = int(c_list[i])
    return c_list



def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    color = get_average(pixels)

    best = 2000000
    #distance = 0
    for ele in pixels:
        distance = get_pixel_dist(ele, color[0], color[1], color[2])
        if distance < best:
            best = distance
    for ele in pixels:
        if get_pixel_dist(ele, color[0], color[1], color[2]) == best:
            return ele


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(images[0].width):
        for y in range(images[0].height):
            pixel = []
            for i in range(len(images)):
                pixel.append(images[i].get_pixel(x, y))
            best = get_best_pixel(pixel)
            best_pixel = result.get_pixel(x, y)
            best_pixel.red = best.red
            best_pixel.green = best.green
            best_pixel.blue = best.blue


    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
