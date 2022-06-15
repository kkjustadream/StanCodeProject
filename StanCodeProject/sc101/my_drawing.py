"""
File: my_drawing
Name: 黃勝弘
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow
WIDTH = 800
HEIGHT = 400

def main():
    """
    Title: Pompompurin
    Cute dog that I usually plat with. I cannot sleep without it! Hope it can be with me forever.
    """
    window = GWindow(WIDTH, HEIGHT, title='pompompurin')
    back_ground(window)
    face(window)
    ears(window)
    hat(window)
    introduce = GLabel('PomPomPurin', x=310, y=110)
    introduce.font = '-25'
    introduce.color = 'white'
    window.add(introduce)


def back_ground(window):
    back = GRect(WIDTH, HEIGHT)
    back.filled = True
    back.color = '#DABEA7'
    back.fill_color = '#DABEA7'
    window.add(back)


def ears(window):
    left_ear = GOval(300, 70,x=40, y=80)
    left_ear.color = '#fefa95'
    left_ear.filled = True
    left_ear.fill_color = '#fffa96'
    window.add(left_ear)
    right_ear = GOval(300, 70, x=460, y=80)
    right_ear.filled = True
    right_ear.fill_color = '#fffa96'
    right_ear.color = '#fefa95'
    window.add(right_ear)


def hat(window):
    hat = GOval(40, 50, x=WIDTH / 2 - 20, y=20)
    hat.filled = True
    hat.fill_color = '#c06a31'
    hat.color = '#965130'
    window.add(hat)
    hat1 = GOval(300, 90, x=250, y=50)
    hat1.filled = True
    hat1.fill_color = '#c06a31'
    hat1.color = '#965130'
    window.add(hat1)


def face(window):
    face = GOval(500, 260, x=150, y=100)
    face.filled = True
    face.color = '#fefa95'
    face.fill_color = '#fffa96'
    window.add(face)
    left_eye = GOval(24, 24, x=280, y=180)
    left_eye.filled = True
    left_eye.color = '#9b4d31'
    left_eye.fill_color = '#9b4d31'
    window.add(left_eye)

    right_eye = GOval(24, 24, x=496, y=180)
    right_eye.filled = True
    right_eye.color = '#9b4d31'
    right_eye.fill_color = '#9b4d31'
    window.add(right_eye)

    nose = GPolygon()
    nose.add_vertex((390, 235))
    nose.add_vertex((390, 243))
    nose.add_vertex((400, 250))
    nose.add_vertex((410, 243))
    nose.add_vertex((410, 235))
    nose.filled = True
    nose.fill_color = '#a66a39'
    nose.color = '#a66a39'
    window.add(nose)

    mouse = GArc(80, 80, 15, -150, x=333, y=230)
    window.add(mouse)

    mouse1 = GArc(80, 80, 165, 150, x=400, y=230)
    window.add(mouse1)

if __name__ == '__main__':
    main()
