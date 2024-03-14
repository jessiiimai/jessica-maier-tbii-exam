# sarahs code 11th lecture (check if it really was 11th)
import tkinter as tk

bg_colour = "#17202A"
text_colour = "#EAECEE"
font = "Helvetica 14"
font_bold = "Helvetica 13 bold"

def send():
    user_message = entry_box.get()
    if user_message:
        text_box.insert(tk.END, f"\nUser: {user_message}")
        if (user_message == "hello"):
            text_box.insert(tk.END, f"\nBot: Hi!")
        else:
            text_box.insert(tk.END, f"\nBot: I am still a work in progress.")
            text_box.insert(tk.END, f"\nBot: I will shut down now.")
            # destroy what was created
            entry_box.destroy()
            send_button.destroy()
    # delete what was entered by the user
    entry_box.delete(0, tk.END)

def send_message(event):
    send()

def create_chatbot(root):
    global entry_box, send_button, text_box

    welcome_label = tk.Label(root, text="Welcome to the Chatbot!", bg=bg_colour, fg=text_colour, font=font_bold, width=30, height=1)
    welcome_label.place(relx=0.5, y=17, anchor=tk.CENTER)  # relx is a relative position

    text_box = tk.Text(root, bg=bg_colour, fg=text_colour, font=font, width=60)
    text_box.place(x=0, y=30, relwidth=1, relheight=1)  # rel etc. is taking up the entire height and width
    text_box.insert(tk.END, "Bot: Hello, what can I do for you?")

    # create a scrollbar
    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1, relx=0.974)

    # create an entry box
    entry_box = tk.Entry(root, bg="#2C3E50", fg=text_colour, font=font, width=35)
    entry_box.place(x=1, rely=0.75)
    entry_box.bind('<Return>', send_message)

    # send button
    send_button = tk.Button(root, text="Send", font=font_bold, command=send, bg="#ABB2B9", width=8)
    send_button.place(x=150, y=580)