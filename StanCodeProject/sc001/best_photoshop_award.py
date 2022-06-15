"""
File: best_photoshop_award.py
Name: 黃勝弘
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

WHITE = 530


def main():
    """
    創作理念： 想成為別人心目中的巨人(好的方面的)
    """
    back = SimpleImage('image_contest/巨人2.png')
    kevin_pic = SimpleImage('image_contest/Image-1 (1).jpg')
    back.make_as_big_as(kevin_pic)
    # make to pic same size
    back.show()
    kevin_pic.show()
    combined_img = combine(back, kevin_pic)
    combined_img.show()


def combine(back, kevin):
    """
    param back: simpleimage, background pic
    param kevin: simpleimage, my pic
    return: simpleimage, edited pic
    """
    for x in range(back.width):
        for y in range(back.height):
            pixel_kevin = kevin.get_pixel(x, y)
            total = pixel_kevin.red + pixel_kevin.green + pixel_kevin.blue
            if total > WHITE:
                # if kevin pic is white change to background pic
                pixel_back = back.get_pixel(x, y)
                pixel_kevin.red = pixel_back.red
                pixel_kevin.green = pixel_back.green
                pixel_kevin.blue = pixel_back.blue
    return kevin


if __name__ == '__main__':
    main()
