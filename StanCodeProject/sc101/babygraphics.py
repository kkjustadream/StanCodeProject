"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)       # space between years
    return GRAPH_MARGIN_SIZE + year_index * x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # draw boundaries
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)   # up
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)  # left
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)    # right
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)   # bottom
    # draw year line + year text
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    rank_distance = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
    no_rank = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS)-1):
            year = YEARS[j]
            next_year = YEARS[j+1]

            if str(year) in name_data[name]:        # str(year)!!!!!
                rank = int(name_data[name][str(year)])
            else:
                rank = 1001  # no data show'*'
            if str(next_year) in name_data[name]:   # str(year)!!!!!
                next_rank = int(name_data[name][str(next_year)])
            else:
                next_rank = 1001  # no data show'*'

            # line's start and end xy coordinate
            x_start = get_x_coordinate(CANVAS_WIDTH, j)
            x_end = get_x_coordinate(CANVAS_WIDTH, j+1)
            if rank > 1000 and next_rank > 1000:
                y_start = no_rank
                y_end = no_rank
                canvas.create_line(x_start, y_start, x_end, y_end, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(x_start+TEXT_DX, y_start, text=str(name)+' '+'*',
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
            elif rank > 1000 > next_rank:
                y_start = no_rank
                y_end = GRAPH_MARGIN_SIZE + next_rank * rank_distance
                canvas.create_line(x_start, y_start, x_end, y_end, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(x_start+TEXT_DX, y_start, text=str(name)+' '+'*',
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
            elif rank < 1000 < next_rank:
                y_start = GRAPH_MARGIN_SIZE + rank * rank_distance
                y_end = no_rank
                canvas.create_line(x_start, y_start, x_end, y_end, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(x_start+TEXT_DX, y_start, text=str(name)+' '+str(rank),
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
            elif rank < 1000 and next_rank < 1000:
                y_start = GRAPH_MARGIN_SIZE + rank * rank_distance
                y_end = GRAPH_MARGIN_SIZE+next_rank*rank_distance
                canvas.create_line(x_start, y_start, x_end, y_end, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(x_start+TEXT_DX, y_start, text=str(name)+' '+str(rank),
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
        # last year's text
        last_year = YEARS[len(YEARS) - 1]
        if str(last_year) in name_data[name]:  # str(year)!!!!!
            last_rank = int(name_data[name][str(last_year)])
        else:
            last_rank = 1001  # no data show'*'
        if last_rank > 1000:
            x_last = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)
            y_last = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_text(x_last + TEXT_DX, y_last, text=str(name)+' '+'*',
                               fill=COLORS[i % 4], anchor=tkinter.SW)
        else:
            x_last = get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1)
            y_last = GRAPH_MARGIN_SIZE + last_rank * rank_distance
            canvas.create_text(x_last + TEXT_DX, y_last, text=str(name) + ' ' + str(last_rank),
                               fill=COLORS[i % 4], anchor=tkinter.SW)








# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
