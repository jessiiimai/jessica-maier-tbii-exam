import tkinter as tk

# saving the data in a list
working_hours = []

# the position we are in the list, it currently starts with entry 0
current_position_inlist = 0
# the amount of items from the list that are shown
shown_items = 8


# a definition to reload the page
# https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
def reload_page(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_workinghours(frame)


# definitions so that we can show not all entrys in the list but iterate through it
def scroll_up(frame):
    global current_position_inlist
    if current_position_inlist > 0:
        current_position_inlist -= 1
        reload_page(frame)


def scroll_down(frame):
    global current_position_inlist
    if current_position_inlist < (len(working_hours)-shown_items):
        current_position_inlist += 1
        reload_page(frame)


# this defines what color will be shown per entry in accordance to the working ratio
def calculate_color(input_hours, input_workedhours):
    if input_hours > input_workedhours:
        return "yellow"
    elif input_workedhours > input_hours:
        return "red"
    else:
        return "green"


# definition for the submit button adds the entrys to our list
def submit_entry(frame, dateentry, workinghourscale, workinghoursdonescale):
    working_hours.append((dateentry.get(), workinghoursdonescale.get(), workinghourscale.get()))
    reload_page(frame)


# definition with all our widgets
def show_workinghours(frame):
    workinghours_header_part1 = tk.Label(frame, text='Here you can track your amount of overwork by saving the',
                                         font='lucinda 10', bg='Pink', fg='Black')
    workinghours_header_part1.place(x=30, y=50)
    workinghours_header_part2 = tk.Label(frame, text='date, the hours you expected to work and actually worked.',
                                         font='lucinda 10', bg='Pink', fg='Black')
    workinghours_header_part2.place(x=30, y=80)

    dateentry = tk.Entry(frame, width=20, font="lucinda 13")
    dateentry.place(x=170, y=250)
    dateentry_label = tk.Label(frame, text="DATE", bg="light blue", font='lucinda 11 bold', fg='Black')
    dateentry_label.place(x=30, y=250)

    scale_workhours = tk.Scale(frame, from_=0, to=50, orient="horizontal", bg="light blue", length=200)
    scale_workhours.place(x=170, y=130)
    workhours_label = tk.Label(frame, text="HOURS NEEDED", bg="light blue", font='lucinda 11 bold', fg='Black')
    workhours_label.place(x=30, y=130)

    scale_workedhours = tk.Scale(frame, from_=0, to=50, orient="horizontal", bg="light blue", length=200)
    scale_workedhours.place(x=170, y=190)
    workedhours_label = tk.Label(frame, text="HOURS WORKED", bg="light blue", font='lucinda 11 bold', fg='Black')
    workedhours_label.place(x=30, y=190)

    submit_button = tk.Button(frame, text="SUBMIT", bg="red", font='lucinda 11 bold', command=lambda: submit_entry(frame, dateentry, scale_workhours, scale_workedhours))
    submit_button.place(x=30, y=290)

    up_button = tk.Button(frame, text="⬆", command=lambda: scroll_up(frame))
    up_button.place(x=300, y=290)
    down_button = tk.Button(frame, text="⬇", command=lambda: scroll_down(frame))
    down_button.place(x=330, y=290)

    trafficlight_canvas = tk.Canvas(frame, bg="light blue", highlightthickness=0, relief='ridge', width=100, height=30*shown_items)
    trafficlight_canvas.place(x=160, y=335)

    row = 340
    canvas_row = 0

    for i in range(current_position_inlist, current_position_inlist+shown_items):
        if i < len(working_hours):
            (d, n, w) = working_hours[i]
            date_label = tk.Label(frame, text=d)
            date_label.place(x=30, y=row)
            row += 30
            ratio_label = tk.Label(frame, text=f"{n}/{w}")
            ratio_label.place(x=110, y=row-30)
            trafficlight_canvas.create_rectangle(0, canvas_row+5, 20, 25+canvas_row, fill=calculate_color(w, n))
            canvas_row += 30


