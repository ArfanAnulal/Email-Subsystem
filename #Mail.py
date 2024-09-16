#Importing the tkinter library
from tkinter import *
import os


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


#Create an instance of tkinter frame
splash_win= Tk()

splash_win['bg'] = 'red'

#Set the title of the window
splash_win.title("Splash Screen")

#Define the size of the window or frame
splash_win.geometry("700x200")

#Remove border of the splash Window

splash_win.overrideredirect(True)
center(splash_win)
#Define the label of the window
splash_label= Label(splash_win, text= "Welcome to voidmail", fg= "yellow",bg='red',
font= ('Grobold', 50)).pack(pady=65)
def mainWin():
   splash_win.destroy()
   os.system('1Main.py')


#Splash Window Timer

splash_win.after(2000, mainWin)

mainloop()
