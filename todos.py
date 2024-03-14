# https://www.geeksforgeeks.org/python-todo-gui-application-using-tkinter/
from tkinter import *
# list to store tasks
tasks_list = []
counter = 1

# I need to rename all of this
# clearing the contents of task number text field
def clear_taskNumberField(taskNumberField):
    taskNumberField.delete(0.0, END)


# clearing the contents of task entry field
def clear_taskField(enterTaskField):
    enterTaskField.delete(0, END)


def insertTask(enterTaskField, textArea):
    global counter

    # get the task string concatenating with new line character
    content = enterTaskField.get() + "\n"
    # store task in the list
    tasks_list.append(content)
    # insert content of task entry field to the text area and add task one by one in below one by one
    textArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    # incremented
    counter += 1
    # function calling for deleting the content of task field
    clear_taskField(enterTaskField)


# function for deleting the specified task
def delete_task(taskNumberField, textArea):
    global counter

    # get the task number, which is required to delete
    number = taskNumberField.get(1.0, END)
    task_no = int(number)
    # deleting the content of task number field
    clear_taskNumberField(taskNumberField)
    # deleted specified task from the list
    tasks_list.pop(task_no - 1)
    # decremented
    counter -= 1
    # whole content of text area widget is deleted
    textArea.delete(1.0, END)
    # rewriting the task after deleting one task at a time
    for i in range(len(tasks_list)):
        textArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])


def show_todolist_widgets(tk, frame):
    # create a label : Enter Your Task
    enterTask = tk.Label(frame, text="Enter Your Task", bg="light green")
    enterTask.place(x=30, y=110)
    # create a text entry box for typing the task
    enterTaskField = tk.Entry(frame)
    enterTaskField.place(x=30, y=140)

    # create a Submit Button
    submit = tk.Button(frame, text="Submit", fg="Black", bg="Red", command=lambda: insertTask(enterTaskField, textArea))
    submit.place(x=30, y=170)

    # create a scroll bar and text area
    scroll_tasks = tk.Scrollbar(frame, orient='vertical')
    scroll_tasks.pack(side="right", fill='y')
    textArea = tk.Text(frame, height=5, width=25, font="lucida 13")
    textArea.place(x=30, y=200)
    scroll_tasks.config(command=textArea.yview)

    # create a label : Delete Task Number
    taskNumber = tk.Label(frame, text="Delete Task Number", bg="blue")
    taskNumber.place(x=30, y=310)
    taskNumberField = tk.Text(frame, height=1, width=2, font="lucida 13")
    taskNumberField.place(x=30, y=340)

    # create a Delete Button and place into the root window
    deletion = tk.Button(frame, text="Delete", fg="Black", bg="Red", command=lambda: delete_task(taskNumberField, textArea))
    deletion.place(x=30, y=370)
