import tkinter
from tkinter import messagebox
import setup
import base64

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
def encrypt_button(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decrypt_button(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt():
    title = entry.get()
    message = text.get("1.0", tkinter.END)
    master_key = entry2.get()

    if len(title) == 0 or len(message) == 0 or len(master_key) == 0:
        messagebox.showwarning(title="Error!", message="Please enter all info!")
    else:
        encrypted_message = encrypt_button(key=master_key, clear=message)

        try:
            with open("SecretNotes.txt", "a") as file:
                file.write(f"\n{title}\n{encrypted_message}")
        except FileNotFoundError:
            with open("SecretNotes.txt", "w") as file:
                file.write(f"\n{title}\n{encrypted_message}")
        finally:
            entry.delete(0, tkinter.END)
            entry2.delete(0, tkinter.END)
            text.delete("1.0", tkinter.END)


def decrypt_note():
    encrypted_message = text.get("1.0", tkinter.END)
    master_key = entry2.get()

    if len(encrypted_message) == 0 or len(master_key) == 0:
        messagebox.showwarning(title="Error!", message="Please enter text and master key!")
    else:
        try:
            decrypt_message = decrypt_button(master_key, encrypted_message)
            text.delete("1.0", tkinter.END)
            text.insert("1.0", decrypt_message)
        except:
            messagebox.showinfo(title="Error", message="Please enter encrypted text")


button = tkinter.Button(command=save_and_encrypt)
button2 = tkinter.Button(command=decrypt_note)
setup.setup_buttons(button=button, button2=button2)

setup.setup_placement(canvas=canvas, label=label, entry=entry, label2=label2, text=text,
                      label3=label3, entry2=entry2, button=button, button2=button2)
screen.mainloop()
