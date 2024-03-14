def show_calculator_widgets(tk, frame_calculator, input_worktime, input_sleeptime, input_careworktime, input_freetime, calculator):
    # Then there is a small explanatory text.
    explanation_part1 = tk.Label(frame_calculator, text="Type in how much time you spend on", font='lucinda 11 bold',
                                 bg='Pink', fg='Black')
    explanation_part1.place(x=30, y=80)

    explanation_part2 = tk.Label(frame_calculator, text="each task and press calculate.", font='lucinda 11 bold',
                                 bg='Pink', fg='Black')
    explanation_part2.place(x=30, y=100)

    # These are input fields for the hours spent on each task of your day to calculate later.

    scale_work = tk.Scale(frame_calculator, from_=0, to=168, orient="horizontal", length=240)
    scale_work.place(x=150, y=130)
    work_label = tk.Label(frame_calculator, text="WORK", font='lucinda 11 bold', fg='Black')
    work_label.place(x=30, y=130)

    scale_sleep = tk.Scale(frame_calculator, from_=0, to=168, orient="horizontal", length=240)
    scale_sleep.place(x=150, y=180)
    sleep_label = tk.Label(frame_calculator, text="SLEEP", font='lucinda 11 bold', fg='Black')
    sleep_label.place(x=30, y=180)

    scale_carework = tk.Scale(frame_calculator, from_=0, to=168, orient="horizontal", length=240)
    scale_carework.place(x=150, y=230)
    carework_label = tk.Label(frame_calculator, text="CARE WORK", font='lucinda 11 bold', fg='Black')
    carework_label.place(x=30, y=230)

    scale_freetime = tk.Scale(frame_calculator, from_=0, to=168, orient="horizontal", length=240)
    scale_freetime.place(x=150, y=280)
    freetime_label = tk.Label(frame_calculator, text="FREE TIME", font='lucinda 11 bold', fg='Black')
    freetime_label.place(x=30, y=280)

    # This creates the calculate button.

    calculate_button = tk.Button(frame_calculator, text="CALCULATE", font='lucinda 15 bold', height=1, width=15,
                                 command=lambda: calculate_worklifebalance(tk, frame_calculator, scale_work, scale_sleep, scale_carework, scale_freetime, calculator))
    calculate_button.place(x=30, y=330)

def calculate_worklifebalance(tk, frame_calculator, input_worktime, input_sleeptime, input_careworktime, input_freetime, calculator):
    # the +1/+4 is for not having the dividing by zero error
    sum_hours = input_worktime.get() + input_sleeptime.get() + input_careworktime.get() + input_freetime.get() + 4
    # From here we create one label for each statement about your input, so the sum and the 4 percentages.

    show_piechart(tk, frame_calculator, (input_worktime.get()+1)/sum_hours, (input_sleeptime.get()+1)/sum_hours, (input_careworktime.get()+1)/sum_hours, (input_freetime.get()+1)/sum_hours)

    # sum_label = tk.Label(frame_calculator, text=f"The sum is {sum_hours}.", font='lucinda 11 bold', fg='Black')
    # sum_label.place(x=30, y=330)

    work_percentage_label = tk.Label(
        frame_calculator, text=f"Work makes up "f"{int(((input_worktime.get()+1)*100)/sum_hours)}% of your time.",
        font='lucinda 9 bold', fg='red')
    work_percentage_label.place(x=30, y=375)

    sleep_percentage_label = tk.Label(
        frame_calculator, text=f"Sleep makes up "f"{int(((input_sleeptime.get()+1)*100)/sum_hours)}% of your time.",
        font='lucinda 9 bold', fg='blue')
    sleep_percentage_label.place(x=30, y=400)

    carework_percentage_label = tk.Label(
        frame_calculator, text=f"Carework makes up "f"{int(((input_careworktime.get()+1)*100)/sum_hours)}% of your time.",
        font='lucinda 9 bold', fg='green')
    carework_percentage_label.place(x=30, y=425)

    freetime_percentage_label = tk.Label(
        frame_calculator, text=f"Freetime makes up "f"{int(((input_freetime.get()+1)*100)/sum_hours)}% of your time.",
        font='lucinda 9 bold', fg="#ED9121")
    freetime_percentage_label.place(x=30, y=450)

    calculator()


def show_piechart(tk, frame, worktime_perc, sleeptime_perc, careworktime_perc, freetime_perc):
    canvas = tk.Canvas(frame, bg="pink", highlightthickness=0, relief='ridge')
    canvas.place(x=180, y=400)
    # position, size, start, degree, color
    work_deg = worktime_perc * 360
    sleep_deg = sleeptime_perc * 360
    care_deg = careworktime_perc * 360
    canvas.create_arc(60, 60, 200, 200, start=0, extent=work_deg, fill="red")
    canvas.create_arc(60, 60, 200, 200, start=work_deg, extent=sleep_deg, fill="blue")
    canvas.create_arc(60, 60, 200, 200, start=work_deg + sleep_deg, extent=care_deg, fill="green")
    canvas.create_arc(60, 60, 200, 200, start=work_deg + sleep_deg + care_deg, extent=360*freetime_perc, fill="#ED9121")