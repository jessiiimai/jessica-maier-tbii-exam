import tkinter as tk
from calculator import *
from todos import *
from habittracker import *
from workinghours import *

# create the GUI and configure it
root = tk.Tk()
root.title('My Friendly Coworker')
root.geometry("405x720")

# variable for background color
bg_colour = "light blue"

# create a frame for every page of the app
frame_homescreen = tk.Frame(root)
frame_homescreen.configure(background=bg_colour)

frame_habittracker = tk.Frame(root)
frame_habittracker.configure(background=bg_colour)

frame_workinghours = tk.Frame(root)
frame_workinghours.configure(background=bg_colour)

frame_todolist = tk.Frame(root)
frame_todolist.configure(background=bg_colour)

frame_calculator = tk.Frame(root)
frame_calculator.configure(background=bg_colour)

# create a header title for the homescreen
homescreen_header_part1 = tk.Label(frame_homescreen, text='Welcome to Your Friendly Coworker,', font='lucinda 15 bold',
                                   bg='Pink', fg='Black')
homescreen_header_part1.place(x=30, y=50)
homescreen_header_part2 = tk.Label(frame_homescreen, text='who can...', font='lucinda 16', bg='Pink', fg='Black')
homescreen_header_part2.place(x=30, y=80)


# code for switching between frames from:
# https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter#:~:text=In%20most%20cases%2C%20you%20need,many%20widgets%20in%20the%20application.
def forget_all():
    frame_homescreen.pack_forget()
    frame_habittracker.pack_forget()
    frame_workinghours.pack_forget()
    frame_todolist.pack_forget()
    frame_calculator.pack_forget()

# when you push the button to get to a page all the frames get forgotten
# and only the corresponding frame gets packed again with all its widgets

def homescreen():
    # switching to Frame1
    forget_all()
    frame_homescreen.pack(fill='both', expand=1)
    root.title("My Friendly Coworker")


def habittracker():
    forget_all()
    frame_habittracker.pack(fill='both', expand=1)
    root.title("Habit Tracker")


def workinghours():
    forget_all()
    frame_workinghours.pack(fill='both', expand=1)
    root.title("Working Time Tracker")


def todolist():
    forget_all()
    frame_todolist.pack(fill='both', expand=1)
    root.title("To Do List")


def calculator():
    forget_all()
    frame_calculator.pack(fill='both', expand=1)
    root.title("Work-Life-Balance Calculator")
    root.update()


# call definitions from the other python files that contain the widgets of the individual pages
show_calculator(frame_calculator, calculator)
show_todolist(tk, frame_todolist)
show_habittracker(frame_habittracker)
show_workinghours(frame_workinghours)

# The following code creates the buttons on the homescreen for every function of the app
# with a little explanatory text directly underneath.

# Habit Tracker
habittracker_button = tk.Button(frame_homescreen, text="Habit Tracker 📈", font='lucinda 15 bold', height=1, width=15,
                                command=lambda: habittracker())
habittracker_button.place(x=10, y=350)
habittracker_explained = tk.Label(frame_homescreen, text='...encourage you to healthier habits.', font='lucinda 8',
                                  bg='Pink', fg='Black')
habittracker_explained.place(x=10, y=400)

# Working Hours Tracker
workinghours_button = tk.Button(frame_homescreen, text="Working Hours🕖", font='lucinda 15 bold', height=1, width=15,
                                command=lambda: workinghours())
workinghours_button.place(x=210, y=350)
workinghours_explained = tk.Label(frame_homescreen, text='...help you track your work hours.', font='lucinda 8',
                                  bg='Pink', fg='Black')
workinghours_explained.place(x=210, y=400)

# To Do List
todolist_button = tk.Button(frame_homescreen, text="To Do List ✔", font='lucinda 15 bold', height=1, width=15,
                            command=lambda: todolist())
todolist_button.place(x=10, y=250)
todolist_explained = tk.Label(frame_homescreen, text='...remind you of your To Dos.', font='lucinda 8',
                              bg='Pink', fg='Black')
todolist_explained.place(x=10, y=300)

# Calculator
calculator_button = tk.Button(frame_homescreen, text="Calculator", font='lucinda 30 bold',
                              command=lambda: calculator())
calculator_button.place(x=80, y=450)
calculator_explained = tk.Label(frame_homescreen, text='...help you calculate your Work-Life-Balance Score.',
                                font='lucinda 8', bg='Pink', fg='Black')
calculator_explained.place(x=75, y=550)


# This code creates the buttons on the taskbar below.

home_button = tk.Button(text="🛖", font='lucinda 20 bold', command=lambda: homescreen())
home_button.place(x=25, y=650)

habittracker_button = tk.Button(text="📈", font='lucinda 20 bold', command=lambda: habittracker())
habittracker_button.place(x=125, y=650)

workhours_button = tk.Button(text="🕖", font='lucinda 20 bold', command=lambda: workinghours())
workhours_button.place(x=225, y=650)

todolist_button = tk.Button(text="✔", font='lucinda 20 bold', command=lambda: todolist())
todolist_button.place(x=325, y=650)

# And the final lines are to execute the code and to start with the homescreen.
homescreen()
root.mainloop()
