import tkinter as tk

working_hours = []

current_position_inlist = 0
shown_items = 8


def reload_page(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack(fill='both', expand=1)
    show_workinghours(frame)

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

def calculate_color(input_hours, input_workedhours):
    if input_hours > input_workedhours:
        return "yellow"
    elif input_workedhours > input_hours:
        return "red"
    else:
        return "green"


def submit_entry(frame, dateentry, workinghourscale, workinghoursdonescale):
    working_hours.append((dateentry.get(), workinghoursdonescale.get(), workinghourscale.get()))
    reload_page(frame)


def show_workinghours(frame):
    workinghours_header_part1 = tk.Label(frame, text='Here you can later track your amount of workhours ',
                                         font='lucinda 11', bg='Pink', fg='Black')
    workinghours_header_part1.place(x=30, y=50)
    workinghours_header_part2 = tk.Label(frame, text='per week to check for possible overtime.',
                                         font='lucinda 11', bg='Pink', fg='Black')
    workinghours_header_part2.place(x=30, y=80)

    dateentry = tk.Entry(frame, width=20, font="lucida 13")
    dateentry.place(x=170, y=250)
    dateentry_label = tk.Label(frame, text="DATE", font='lucinda 11 bold', fg='Black')
    dateentry_label.place(x=30, y=250)

    scale_workhours = tk.Scale(frame, from_=0, to=50, orient="horizontal", length=200)
    scale_workhours.place(x=170, y=130)
    workhours_label = tk.Label(frame, text="HOURS NEEDED", font='lucinda 11 bold', fg='Black')
    workhours_label.place(x=30, y=130)

    scale_workedhours = tk.Scale(frame, from_=0, to=50, orient="horizontal", length=200)
    scale_workedhours.place(x=170, y=190)
    workedhours_label = tk.Label(frame, text="HOURS WORKED", font='lucinda 11 bold', fg='Black')
    workedhours_label.place(x=30, y=190)

    submit_button = tk.Button(frame, text="SUBMIT", command=lambda:submit_entry(frame,dateentry, scale_workhours, scale_workedhours))
    submit_button.place(x=30, y=290)

    up_button = tk.Button(frame, text="⬆", command=lambda:scroll_up(frame))
    up_button.place(x=100, y=290)
    down_button = tk.Button(frame, text="⬇", command=lambda:scroll_down(frame))
    down_button.place(x=130, y=290)

    trafficlight_canvas = tk.Canvas(frame, bg="yellow", highlightthickness=0, relief='ridge', width=100, height=30*shown_items)
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


