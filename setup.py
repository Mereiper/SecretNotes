def setup_screen(screen):
    screen.minsize(300, 500)
    screen.maxsize(300, 500)
    screen.title("Secret Notes")
    screen.config(padx=10, pady=10)


def setup_labels(label, label2, label3):
    label.config(text="Enter your title", font="Arial", pady=10)
    label2.config(text="Enter your Secret", font="Arial", pady=5)
    label3.config(text="Enter master key", font="Arial", pady=5)


def setup_texts(entry, entry2, text):
    entry.config(width=30)
    entry2.config(width=20)
    text.config(width=30, height=10)


def setup_buttons(button, button2):
    button.config(text="Save & Encrypt")
    button2.config(text="Decrypt")


def setup_placement(canvas, label, entry, label2, text, label3, entry2, button, button2):
    canvas.pack()
    label.pack()
    entry.pack()
    label2.pack()
    text.pack()
    label3.pack()
    entry2.pack()
    button.pack()
    button2.pack()
