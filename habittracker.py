import tkinter as tk

# a dictionary to save the data of the submitted habits and the frequency for the checkboxes
habit_data = {"3/2024": [("example", [True, False])]}
# saving the current month as default
current_month = "3/2024"


# definition to reload the page
# https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
def reload_page(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_habittracker(frame)


# definition to delete a submitted habit from the dictionary
def delete_habit(frame, habit_index):
    del habit_data[current_month][habit_index]
    reload_page(frame)


# definition for the clicked checkboxes
def is_clicked(i, j):
    habit_data[current_month][j][1][i] = not habit_data[current_month][j][1][i]


# definition to submit a new habit to the dictionary
def generate_new_habit(frame, frequency, name):
    habit_data[current_month].append((name, frequency * [False]))
    reload_page(frame)


# definition to reload the page and open a new list for the next month
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

    reload_page(frame)


# definition for changing to the prior month and if not done yet adding another list for that month
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

    reload_page(frame)


# a definition for all our widgets in the frame
def show_habittracker(frame):
    habittracker_header_part1 = tk.Label(frame, text='Here you can track your habits by submitting a ',
                                         font='lucinda 11', bg='Pink', fg='Black')
    habittracker_header_part1.place(x=30, y=50)
    habittracker_header_part2 = tk.Label(frame, text='new habit and ticking the ones you did.',
                                         font='lucinda 11', bg='Pink', fg='Black')
    habittracker_header_part2.place(x=30, y=80)

    m_header = tk.Label(frame, text="Enter Your Habit for the Week!", bg="light blue")
    m_header.place(x=30, y=160)
    # create a text entry box for typing the task
    m_entry = tk.Entry(frame)
    m_entry.place(x=30, y=190)
    m_numbertext = tk.Label(frame, text="Enter the frequency", bg="light blue")
    m_numbertext.place(x=30, y=220)
    m_number = tk.Entry(frame, width=2, font="lucida 13")
    m_number.place(x=30, y=250)

    month_label = tk.Label(frame, text=current_month, bg="light blue")
    month_label.place(x=58, y=122)

    # create buttons
    submit = tk.Button(frame, text="Submit", fg="Black", bg="Red", command=lambda: generate_new_habit(frame, int(m_number.get()), m_entry.get()))
    submit.place(x=30, y=290)
    decrement_m = tk.Button(frame, text="⬅", command=lambda: decrement_month(frame, month_label))
    decrement_m.place(x=30, y=120)
    increment_m = tk.Button(frame, text="➡", command=lambda: increment_month(frame, month_label))
    increment_m.place(x=100, y=120)

    # a for loop to create the habit labels and checkboxes according to the data stored in the dictionary habit_data
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
            # code to make checkboxes: https://pythonbasics.org/tkinter-checkbox/
            checkbox = tk.Checkbutton(frame, onvalue=1, offvalue=0, command=lambda a=i, b=j: is_clicked(a, b))
            checkbox.place(x=column+100, y=row - 60)
            column += 20
            if chkbxs == True:
                # select the checkbox when it is on True, means the user selected it
                checkbox.select()
            i += 1
        column = 30
        j += 1


