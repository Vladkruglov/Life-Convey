'''
Модуль для отображения того, что происходит в игре "Жизнь"
'''

import tkinter

from constants import COORD_MAX_X, COORD_MAX_Y, SIZE_OF_THE_CELL_X, SIZE_OF_THE_CELL_Y

t = tkinter.Tk()
c = tkinter.Canvas(t,height = COORD_MAX_Y,width = COORD_MAX_X)
c.pack()

def field(generation):
    """Принимает список всех генераций
    Создаёт поле для игры"""
    c.delete("all")
    generation = list(generation)
    for i in range(0, COORD_MAX_Y, SIZE_OF_THE_CELL_Y):
        c.create_line(i, COORD_MAX_X, i, 0, fill = "grey")

    for i in range(0, COORD_MAX_X, SIZE_OF_THE_CELL_X):
        c.create_line(COORD_MAX_Y, i, 0,  i, fill = "grey") 

    for (x, y) in generation:
        c.create_rectangle(x * SIZE_OF_THE_CELL_X, y * SIZE_OF_THE_CELL_Y,
          x * SIZE_OF_THE_CELL_X + SIZE_OF_THE_CELL_X, y * SIZE_OF_THE_CELL_Y + SIZE_OF_THE_CELL_Y,  fill = "black")
    c.update()
    c.update_idletasks()

    import time