"""
File: blur.py
Name: 黃勝弘
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: simpleimage, old img
    :return: simpleimage, blurred img
    """
    # Todo: create a new blank img that is as big as the original one

    new_img = SimpleImage.blank(img.width, img.height)
    # new blank
    new_img.make_as_big_as(img)
    # loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            new_p = new_img.get_pixel(x, y)
            # Todo: get pixel of new_img at x,y
            # belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                old_p = img.get_pixel(x + 1, y)
                old_p2 = img.get_pixel(x + 1, y + 1)
                old_p3 = img.get_pixel(x, y + 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red) // 3
                new_p.green = (old_p.green + old_p2.green + old_p3.green) // 3
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue) // 3
                # get pixel at the top-left corner of the image.

            elif x == img.width and y == 0:
                old_p = img.get_pixel(x - 1, y)
                old_p2 = img.get_pixel(x - 1, y + 1)
                old_p3 = img.get_pixel(x, y + 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red) // 3
                new_p.green = (old_p.green + old_p2.green + old_p3.green) // 3
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue) // 3
                # get pixel at the top-right corner of the image.

            elif x == 0 and y == img.height:
                old_p = img.get_pixel(x, y - 1)
                old_p2 = img.get_pixel(x + 1, y - 1)
                old_p3 = img.get_pixel(x + 1, y)
                new_p.red = (old_p.red + old_p2.red + old_p3.red) // 3
                new_p.green = (old_p.green + old_p2.green + old_p3.green) // 3
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue) // 3
                # get pixel at the bottom-left corner of the image

            elif x == img.width and y == img.height:
                old_p = img.get_pixel(x, y - 1)
                old_p2 = img.get_pixel(x - 1, y - 1)
                old_p3 = img.get_pixel(x - 1, y)
                new_p.red = (old_p.red + old_p2.red + old_p3.red) // 3
                new_p.green = (old_p.green + old_p2.green + old_p3.green) // 3
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue) // 3
                # get pixel at the bottom-right corner of the image

            elif y == 0 and 0 < x < img.width - 1:
                old_p = img.get_pixel(x-1, y)
                old_p2 = img.get_pixel(x, y)
                old_p3 = img.get_pixel(x + 1, y)
                old_p4 = img.get_pixel(x - 1, y + 1)
                old_p5 = img.get_pixel(x, y + 1)
                old_p6 = img.get_pixel(x + 1, y + 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red + old_p4.red + old_p5.red + old_p6.red) // 6
                new_p.green = (old_p.green + old_p2.green + old_p3.green + old_p4.green + old_p5.green + old_p6.green) // 6
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p5.blue + old_p6.blue) // 6
                # get top edge's pixels (without two corners)

            elif 0 < x <= img.width - 1 and y == img.height:
                old_p = img.get_pixel(x - 1, y)
                old_p2 = img.get_pixel(x, y)
                old_p3 = img.get_pixel(x + 1, y)
                old_p4 = img.get_pixel(x - 1, y - 1)
                old_p5 = img.get_pixel(x, y - 1)
                old_p6 = img.get_pixel(x + 1, y - 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red + old_p4.red + old_p5.red + old_p6.red) // 6
                new_p.green = (old_p.green + old_p2.green + old_p3.green + old_p4.green + old_p5.green + old_p6.green) // 6
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p5.blue + old_p6.blue) // 6
                # get bottom edge's pixels (without two corners)

            elif x == 0 and 0 < y < img.height - 1:
                old_p = img.get_pixel(0, y - 1)
                old_p2 = img.get_pixel(0, y)
                old_p3 = img.get_pixel(0, y + 1)
                old_p4 = img.get_pixel(1, y - 1)
                old_p5 = img.get_pixel(1, y)
                old_p6 = img.get_pixel(1, y + 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red + old_p4.red + old_p5.red + old_p6.red) // 6
                new_p.green = (old_p.green + old_p2.green + old_p3.green + old_p4.green + old_p5.green + old_p6.green) // 6
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p5.blue + old_p6.blue) // 6
                # get left edge's pixels (without two corners)

            elif x == img.width and 0 < y <= img.height - 1:
                old_p = img.get_pixel(x, y - 1)
                old_p2 = img.get_pixel(x, y)
                old_p3 = img.get_pixel(x, y + 1)
                old_p4 = img.get_pixel(x + 1, y - 1)
                old_p5 = img.get_pixel(x + 1, y)
                old_p6 = img.get_pixel(x + 1, y + 1)
                new_p.red = (old_p.red + old_p2.red + old_p3.red + old_p4.red + old_p5.red + old_p6.red) // 6
                new_p.green = (old_p.green + old_p2.green + old_p3.green + old_p4.green + old_p5.green + old_p6.green) // 6
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p5.blue + old_p6.blue) // 6
                # # get right edge's pixels (without two corners)

            elif 0 < x < img.width - 1 and 0 < y < img.height - 1:
                old_p = img.get_pixel(x + 1, y)
                old_p2 = img.get_pixel(x - 1, y - 1)
                old_p3 = img.get_pixel(x - 1, y)
                old_p4 = img.get_pixel(x, y - 1)
                old_p5 = img.get_pixel(x + 1, y - 1)
                old_p6 = img.get_pixel(x - 1, y + 1)
                old_p7 = img.get_pixel(x, y + 1)
                old_p8 = img.get_pixel(x + 1, y + 1)
                old_p9 = img.get_pixel(x, y)
                new_p.red = (old_p.red + old_p2.red + old_p3.red + old_p4.red + old_p5.red + old_p6.red + old_p7.red + old_p8.red + old_p9.red) // 9
                new_p.green = (old_p.green + old_p2.green + old_p3.green + old_p4.green + old_p5.green + old_p6.green + old_p7.green + old_p8.green + old_p9.green) // 9
                new_p.blue = (old_p.blue + old_p2.blue + old_p3.blue + old_p4.blue + old_p5.blue + old_p6.blue + old_p7.blue + old_p8.blue + old_p9.blue) // 9
                # Inner pixels.

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
