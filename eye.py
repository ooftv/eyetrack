import tkinter as tk
from PIL import Image

gui = tk.Tk()
gui.geometry("150x200")

pupil_column = 6
pupil_row = 4

top_eye = tk.Button(gui, text = '')
top_eye.grid(row = 1, column = 4, columnspan = 4)

row_two_left = tk.Button(gui, text = '')
row_two_left.grid(row = 2, column = 2, columnspan = 2)
row_two_right = tk.Button(gui, text = '')
row_two_right.grid(row = 2, column =  8, columnspan = 2)

row_three_left = tk.Button(gui, text = '')
row_three_left.grid(row = 3, column =  1, columnspan = 2)
row_three_right = tk.Button(gui, text = '')
row_three_right.grid(row = 3, column =  9, columnspan = 2)

row_four_left = tk.Button(gui, text = '')
row_four_left.grid(row = 4, column =  1, columnspan = 1)
row_four_right = tk.Button(gui, text = '')
row_four_right.grid(row = 4, column =  10, columnspan = 1)
pupil = tk.Button(gui, text = '')
pupil.grid(row = pupil_row, column = pupil_column, columnspan = 1)

row_five_left = tk.Button(gui, text = '')
row_five_left.grid(row = 5, column =  1, columnspan = 2)
row_five_right = tk.Button(gui, text = '')
row_five_right.grid(row = 5, column =  9, columnspan = 2)

row_six_left = tk.Button(gui, text = '')
row_six_left.grid(row = 6, column =  2, columnspan = 2)
row_six_right = tk.Button(gui, text = '')
row_six_right.grid(row = 6, column =  8, columnspan = 2)

row_seven = tk.Button(gui, text = '')
row_seven.grid(row = 7, column =  4, columnspan = 4)

gui.mainloop()











#class Eye:

#this needs to be an object, but for now just sketch
