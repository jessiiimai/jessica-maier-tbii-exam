# https://pythonbasics.org/tkinter-checkbox/
import tkinter as tk

habit_data = {
    "3/2024": [("joggen", [True, False]), ("reading", [False, False, False, False])],
    "4/2024": [("weighlift", [False])]
}

current_month = "3/2024"

def delete_habit(frame, habit_index):
    del habit_data[current_month][habit_index]
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_habittracker(frame)


def is_clicked(i, j):
    habit_data[current_month][j][1][i] = not habit_data[current_month][j][1][i]


def generate_new_habit(frame, frequency, name):
    habit_data[current_month].append((name, frequency * [False]))
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_habittracker(frame)


def increment_month(frame, month_label):
    global current_month
    m, y = current_month.split("/")
    m = int(m) + 1
    if m > 12:
        y = int(y) + 1
        m = 1
    current_month = str(m) + "/" + str(y)
    month_label.config(text=current_month)

    if current_month not in habit_data:
        habit_data[current_month] = []

    # https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_habittracker(frame)


def decrement_month(frame, month_label):
    global current_month
    m, y = current_month.split("/")
    m = int(m) - 1
    if m < 1:
        y = int(y) - 1
        m = 12
    current_month = str(m) + "/" + str(y)
    month_label.config(text=current_month)

    if current_month not in habit_data:
        habit_data[current_month] = []

    # https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_habittracker(frame)


def show_habittracker(frame):
    frame.configure(background="red")

    w_header = tk.Label(frame, text="Enter Your Habit for the Week!", bg="light green")
    w_header.place(x=30, y=160)
    # create a text entry box for typing the task
    w_entry = tk.Entry(frame)
    w_entry.place(x=30, y=190)
    w_numbertext= tk.Label(frame, text="Enter the frequency", bg="light green")
    w_numbertext.place(x=30, y=220)
    w_number = tk.Entry(frame, width=2, font="lucida 13")
    w_number.place(x=30, y=250)

    # create a Submit Button
    submit_weekly = tk.Button(frame, text="Submit", fg="Black", bg="Red", command=lambda: generate_new_habit(frame, int(w_number.get()), w_entry.get()))
    submit_weekly.place(x=30, y=280)

    month_label = tk.Label(frame, text=current_month)
    month_label.place(x=40, y=110)

    decrement_week = tk.Button(frame, command=lambda: decrement_month(frame, month_label))
    decrement_week.place(x=30, y=110)

    increment_weeks = tk.Button(frame, command=lambda: increment_month(frame, month_label))
    increment_weeks.place(x=90, y=110)

    row = 330
    column = 30
    j = 0
    for habit in habit_data[current_month]:
        new_habit = tk.Label(frame, text=habit[0])
        new_habit.place(x=column, y=row)
        delete_habit_button = tk.Button(frame, text="❌", command=lambda a=j: delete_habit(frame, a))
        delete_habit_button.place(x=column, y=row+30)
        row += 60
        i = 0
        for chkbxs in habit[1]:
            # fixed variable source
            checkbox = tk.Checkbutton(frame, onvalue=1, offvalue=0, command=lambda a=i, b=j: is_clicked(a, b))
            checkbox.place(x=column+100, y=row - 60)
            column += 20
            if chkbxs == True:
                # select the checkbox when it is on True, means the user selected it
                checkbox.select()
            i += 1
        column = 30
        j += 1


