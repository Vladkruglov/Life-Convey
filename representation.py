'''
Модуль для отображения того, что происходит в игре "Жизнь"
'''
import time
import tkinter

from constants import COORD_MAX_X, COORD_MAX_Y, SIZE_OF_THE_CELL, NUM_OF_CELLS_IN_A_ROW

t = tkinter.Tk()
c = tkinter.Canvas(t,height = COORD_MAX_Y,width = COORD_MAX_X)
c.pack()

def field(generation):
    """Принимает список всех генераций
    Создаёт поле для игры"""
    c.delete("all")
    generation = list(generation)
    for i in range(0, COORD_MAX_Y, SIZE_OF_THE_CELL):
        c.create_line(i, COORD_MAX_X, i, 0, fill = "grey")

    for i in range(0, COORD_MAX_X, SIZE_OF_THE_CELL):
        c.create_line(COORD_MAX_Y, i, 0,  i, fill = "grey") 
    c.update()

    for (x, y) in generation:
        c.create_rectangle(x * SIZE_OF_THE_CELL, y * SIZE_OF_THE_CELL,
          x * SIZE_OF_THE_CELL + SIZE_OF_THE_CELL, y * SIZE_OF_THE_CELL + SIZE_OF_THE_CELL,  fill = "black")
    c.update()
    c.update_idletasks()
    

