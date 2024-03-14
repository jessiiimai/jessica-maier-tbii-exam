from tkinter import *
# list to store tasks
tasks_list = []
counter = 1

# this code is from:
# https://www.geeksforgeeks.org/python-todo-gui-application-using-tkinter/

# clearing the contents of task number text entry
def clear_contenttasknumber(tasknumber_entry):
    tasknumber_entry.delete(0.0, END)


# clearing the contents of task entry
def clear_contenttask(task_entry):
    task_entry.delete(0, END)


# insert a todo into our list
def insert_todo(task_entry, textArea):
    global counter
    content = task_entry.get() + "\n"
    tasks_list.append(content)
    textArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_contenttask(task_entry)


# function for deleting the specified task
def delete_todo(tasknumber_entry, textArea):
    global counter
    number = tasknumber_entry.get(1.0, END)
    task_no = int(number)
    clear_contenttasknumber(tasknumber_entry)
    tasks_list.pop(task_no - 1)
    counter -= 1
    textArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        textArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])


# function for showing all the widgets
def show_todolist(tk, frame):
    todolist_header_part1 = tk.Label(frame, text='Here you can note down your current todos.',
                                     font='lucinda 11', bg='Pink', fg='Black')
    todolist_header_part1.place(x=30, y=75)

    enter_label = tk.Label(frame, text="Enter Your Task", bg="light blue")
    enter_label.place(x=30, y=110)
    task_entry = tk.Entry(frame)
    task_entry.place(x=30, y=140)

    # create a Submit Button
    submit = tk.Button(frame, text="Submit", fg="Black", bg="Red", command=lambda: insert_todo(task_entry, textArea))
    submit.place(x=30, y=170)

    # create a scroll bar and text area
    scroll_tasks = tk.Scrollbar(frame, orient='vertical')
    scroll_tasks.pack(side="right", fill='y')
    textArea = tk.Text(frame, height=5, width=25, font="lucida 13")
    textArea.place(x=30, y=200)
    scroll_tasks.config(command=textArea.yview)

    # create a label : Delete Task Number
    taskNumber = tk.Label(frame, text="Type in the number of the task you want to delete.", bg="light blue")
    taskNumber.place(x=30, y=310)
    tasknumber_entry = tk.Text(frame, height=1, width=2, font="lucinda 13")
    tasknumber_entry.place(x=30, y=340)

    # create a Delete Button and place into the root window
    deletion = tk.Button(frame, text="Delete", fg="Black", bg="Red", command=lambda: delete_todo(tasknumber_entry, textArea))
    deletion.place(x=30, y=370)
