from tkinter import *
from tkinter import messagebox
import pyperclip as clipboard
from PIL import Image,ImageTk

IMAGE_APP_URL = r'./img/caesar-cipher.ico'
BG = 'BLACK'
FONT_COLOR = '#009000'
FONT_TITLE = ('Arial', 20)
FONT_BODY = ('Arial', 10)
AUTHOR_FONT = ('Arial', 7)
BORDER_SIZE = 3
BTN_WIDTH = 12
ENTRY_IPADY = 2
IMG_URL = './img/caesar-cipher.png'

def caesar(start_text, shift_amount, cipher_direction):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif char not in alphabet:
                end_text += char

    result_input.delete(0, END)
    result_input.insert(0, end_text)


def encrypt():
    try:
        if len(message_input.get()) < 1:
            messagebox.showerror(title='Error', message='Inserte texto en el campo de "Mensaje"')
        else:
            caesar(message_input.get().lower(), int(key_input.get()), 'encode')
    except ValueError:
        messagebox.showerror(title='Error', message='Inserte un número en el campo de "Clave (Key)"')


def decrypt():
    try:
        if len(message_input.get()) < 1:
            messagebox.showerror(title='Error', message='Inserte texto en el campo de "Mensaje"')
        else:
            caesar(message_input.get().lower(), int(key_input.get()), 'decode')
    except ValueError:
        messagebox.showerror(title='Error', message='Inserte un número en el campo de "Clave (Key)"')


def copy_result():
    clipboard.copy(result_input.get())


def clean_message_field():
    message_input.delete(0, END)

window = Tk()
window.title('Cifrado César')
window.minsize(height=250, width=500)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.iconbitmap(IMAGE_APP_URL)
window.configure(bg=BG)

canvas = Canvas(window, width = 50, height = 50, highlightbackground=BG, bg=BG)
canvas.grid(column=0, row=0)

img = Image.open(IMG_URL)
img_resized = img.resize((40, 40), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(img_resized)

canvas.create_image(28,25, anchor=CENTER, image=new_img)

title_label = Label(window, text='Cifrado César', bg=BG, fg=FONT_COLOR, font=FONT_TITLE)
title_label.grid(column=1, row=0, columnspan=2)

author_label = Label(window, text='© MVE10',bg=BG, fg=FONT_COLOR, font=AUTHOR_FONT)
author_label.grid(column=3, row=0)

message_label = Label(window, text='Mensaje:', bg=BG, fg=FONT_COLOR, font=FONT_BODY)
message_label.grid(column=0, row=1)
message_input = Entry(window)
message_input.grid(column=1, row=1, columnspan=2, sticky='we', ipady=ENTRY_IPADY)
message_input.bind('<Return>', (lambda event: decrypt()))

clean_message_btn_border = Frame(window, highlightbackground=FONT_COLOR, highlightthickness=BORDER_SIZE, bd=0)
clean_message_btn_border.grid(column=3, row=1)
clean_message_btn = Button(clean_message_btn_border, text='Limpiar', command=clean_message_field, fg=FONT_COLOR, bg=BG, borderwidth=0, width=BTN_WIDTH)
clean_message_btn.grid(column=3, row=1)
clean_message_btn.bind('<Return>', (lambda event: clean_message_field()))

key_label = Label(window, text='Código (Key):', bg=BG, fg=FONT_COLOR, font=FONT_BODY)
key_label.grid(column=0, row=2)
key_input = Entry(window)
key_input.grid(column=1, row=2, sticky='we', ipady=ENTRY_IPADY)
key_example_label = Label(window, text='Ejemplo: 5', bg=BG, fg=FONT_COLOR, font=FONT_BODY)
key_example_label.grid(column=2, row=2, sticky='we')
key_input.bind('<Return>', (lambda event: encrypt()))

encrypt_btn_border = Frame(window, highlightbackground=FONT_COLOR, highlightthickness=BORDER_SIZE, bd=0)
encrypt_btn_border.grid(column=1, row=3)
encrypt_btn = Button(encrypt_btn_border, text='Encriptar', command=encrypt, fg=FONT_COLOR, bg=BG, borderwidth=0, width=BTN_WIDTH)
encrypt_btn.grid(column=1, row=3)
encrypt_btn.bind('<Return>', (lambda event: encrypt()))

decrypt_btn_border = Frame(window, highlightbackground=FONT_COLOR, highlightthickness=BORDER_SIZE, bd=0)
decrypt_btn_border.grid(column=2, row=3)
decrypt_btn = Button(decrypt_btn_border, text='Desencriptar', command=decrypt, fg=FONT_COLOR, bg=BG, borderwidth=0, width=BTN_WIDTH)
decrypt_btn.grid(column=2, row=3)
decrypt_btn.bind('<Return>', (lambda event: decrypt()))

result_label = Label(window, text='Resultado:', bg=BG, fg=FONT_COLOR, font=FONT_BODY)
result_label.grid(column=0, row=4)
result_input = Entry(window)
result_input.grid(column=1, row=4, columnspan=2, sticky='we', ipady=ENTRY_IPADY)

copy_btn_border = Frame(window, highlightbackground=FONT_COLOR, highlightthickness=BORDER_SIZE, bd=0)
copy_btn_border.grid(column=3, row=4)
copy_btn = Button(copy_btn_border, text='Copiar', command=copy_result, fg=FONT_COLOR, bg=BG, borderwidth=0, width=BTN_WIDTH)
copy_btn.grid(column=3, row=4)
copy_btn.bind('<Return>', (lambda event: copy_result()))

window.mainloop()