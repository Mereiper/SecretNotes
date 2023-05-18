import tkinter
import setup

# Screen
screen = tkinter.Tk()
setup.setup_screen(screen)

# Image
image = tkinter.PhotoImage(file='top-secret.png')
canvas = tkinter.Canvas(height=80, width=80)
canvas.create_image(50, 50, image=image)

# Labels
label = tkinter.Label()
label2 = tkinter.Label()
label3 = tkinter.Label()
setup.setup_labels(label=label, label2=label2, label3=label3)

# Texts
entry = tkinter.Entry()
entry2 = tkinter.Entry()
text = tkinter.Text()
setup.setup_texts(entry=entry, entry2=entry2, text=text)

# Buttons
button = tkinter.Button()
button2 = tkinter.Button()
setup.setup_buttons(button=button, button2=button2)

setup.setup_placement(canvas=canvas, label=label, entry=entry, label2=label2, text=text,
                      label3=label3, entry2=entry2, button=button, button2=button2)
screen.mainloop()
