"""
File: mirror_lake.py
Name: 黃勝弘
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage
    :return: SimpleImage
    """
    lake = SimpleImage(filename)
    b_lake = SimpleImage.blank(lake.width, lake.height*2)
    # make a new zone(nothing inside now)
    for x in range(lake.width):
        # why cannot b.lake.width?
        for y in range(lake.height):
            lake_p = lake.get_pixel(x, y)
            b_lake_p = b_lake.get_pixel(x, y)
            b_lake_p.red = lake_p.red
            b_lake_p.green = lake_p.green
            b_lake_p.blue = lake_p.blue
            # only fill same size as original pic, need to fill pic under

            b_lake_p2 = b_lake.get_pixel(x, b_lake.width - 1 - y)
            b_lake_p2.red = lake_p.red
            b_lake_p2.green = lake_p.green
            b_lake_p2.blue = lake_p.blue
    return b_lake


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
