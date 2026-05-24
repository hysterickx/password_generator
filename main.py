import customtkinter as ctk
from random import choice
from tkinter import messagebox
from pyperclip import copy

ctk.set_appearance_mode ("dark")

app = ctk.CTk()
app.title ('Парольчики')
app.geometry ('500x700+900+300')
app.resizable (False, False)
app.config (bg='#ffcc66')
app.attributes ('-alpha', 0.8)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
waitings = ['Мне нужно\n несколько секундочек...', 'Дайте мне\n немножечко времени...', 'Почти готово...', 'Секундочку...']

def clear_all():
    for widget in app.winfo_children():
        widget.destroy()

def select_all(box1, box2, box3, box4, box5):
    for check in [box1, box2, box3, box4, box5]:
        check.select()

def deselect_all(box1, box2, box3, box4, box5):
    for check in [box1, box2, box3, box4, box5]:
        check.deselect()

def end():
    clear_all()
    label = ctk.CTkLabel (app, text = 'До новых встреч!', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 23, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after(5000, app.destroy)

def repeat():
    clear_all()
    label = ctk.CTkLabel (app, text = 'Запускаю процесс...', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 23, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after(5000, filters)

def result(passwords):
    clear_all()
    frame1 = ctk.CTkFrame(app, bg_color = '#ffcc66', fg_color = '#ffcc66')
    frame1.place(relx = 0, rely = 0, relwidth = 0.7, relheight = 0.7)

    frame2 = ctk.CTkFrame(app, bg_color = '#ffcc66', fg_color = '#ffcc66')
    frame2.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 0.7)

    def copy_all():
        copy (passwords)
        button2.configure (text = 'Скопировано', text_color_disabled = '#000000', state = 'disabled', fg_color = '#ffff99')
        button2.after(1000, lambda: button2.configure(text = 'Copy all', state = 'normal', fg_color = '#ffffff', text_color = '#000000'))

    def copy_action (text, button):
        copy(text)
        button.configure (text = '✅', text_color_disabled = '#000000', state = 'disabled', fg_color = '#ffff99')
        button.after(1000, lambda: button.configure(text = 'Copy', state = 'normal', fg_color = '#ffffff', text_color = '#000000'))

    for i in passwords:
        label = ctk.CTkLabel (frame1, text = i, bg_color = '#ffcc66',
        text_color = '#000000', font = ('Arial', 23, 'bold'))
        label.pack(side = 'top', expand = True, fill = 'both')

        button = ctk.CTkButton (frame2, width = 120, height = 30, text = 'Copy', bg_color = '#ffcc66', fg_color = '#ffffff',
        hover_color = '#996633', corner_radius = 40,  text_color = '#000000', font = ('Arial', 18, 'bold'))
        button.configure(command = lambda text = i, but = button: copy_action(text, but))
        button.pack(side = 'top', expand = True)

    button2 = ctk.CTkButton (app, width = 200, height = 30, corner_radius = 20, text = 'Copy all', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = copy_all)
    button2.place(relx = 0.5, rely = 0.75, anchor = 'c')

    label2 = ctk.CTkLabel (app, text = 'Хотите повторить?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 23, 'bold'))
    label2.place(relx = 0.5, rely = 0.85, anchor = 'c')

    button3 = ctk.CTkButton (app, width = 100, height = 50, corner_radius = 40, text = 'Да', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = repeat)
    button3.place(relx = 0.35, rely = 0.95, anchor = 'c')

    button4 = ctk.CTkButton (app, width = 100, height = 50, corner_radius = 40, text = 'Нет', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = end)
    button4.place(relx = 0.65, rely = 0.95, anchor = 'c')

def create(check1, check2, check3, check4, check5, count, lenght):
    clear_all()

    chars = ''
    symbols = [digits, lowercase_letters, uppercase_letters, punctuation]
    passwords = []
    value = 0

    for i in [check1, check2, check3, check4]:
        if i == 1:
            chars += symbols[value]
        value += 1

    if check5 == 1:
         for j in 'i, I, l, L, 1, !, o, O, 0':
            if j in chars:
                chars = chars.replace(j, '')

    for k in range (count):
        password = ''
        for m in range (lenght):
            password += choice(chars)
        passwords.append(password)

    label = ctk.CTkLabel (app, text = choice(waitings), bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after (5000, lambda: result(passwords))

def check_input(check1, check2, check3, check4, check5, count, lenght):
    value = 0
    for i in [check1, check2, check3, check4]:
        if i == 0:
            value += 1
    if value == 4:
        messagebox.showinfo ('Ошибочка', 'Не выбран ни один тип символов')
    elif len(count) == 0 or len(lenght) == 0:
        messagebox.showinfo ('Ошибочка', 'Не все значения введены')
    elif count.isdigit() == False or lenght.isdigit() == False:
        messagebox.showinfo ('Ошибочка', 'Для ввода допускаются только циферки')
    elif int(count) < 1:
        messagebox.showinfo ('Ошибочка', 'Нужен хотя бы 1 пароль')
    elif int(lenght) < 5:
        messagebox.showinfo ('Ошибочка', 'Недостаточная длина пароля')
    elif int(count) > 10:
        messagebox.showinfo ('Ошибочка', 'Слишком много паролей')
    elif int(lenght) > 20:
        messagebox.showinfo ('Ошибочка', 'Слишком длинный пароль')
    else:
        create(check1, check2, check3, check4, check5, int(count), int(lenght))

def filters():
    clear_all()

    label = ctk.CTkLabel (app, text = 'Сколько паролей\n нужно сгенерировать?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.1, anchor = 'c')

    label = ctk.CTkLabel (app, text = '(Введите значение от 1 до 10)', bg_color = '#ffcc66',
    text_color = '#000000', height = 5, font = ('Arial', 15))
    label.place(relx = 0.5, rely = 0.16, anchor = 'c')

    label = ctk.CTkLabel (app, text = 'Необходимая длина пароля?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    label = ctk.CTkLabel (app, text = '(Введите значение от 5 до 20)', bg_color = '#ffcc66',
    text_color = '#000000', height = 5, font = ('Arial', 15))
    label.place(relx = 0.5, rely = 0.35, anchor = 'c')

    label = ctk.CTkLabel (app, text = 'Какие символы использовать?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    entry1 = ctk.CTkEntry (app, width = 100, height = 30, border_width = 0,  corner_radius = 40, justify = 'c',
    fg_color = '#ffffff', bg_color = '#ffcc66', text_color = '#000066', font = ('Arial', 20, 'bold'))
    entry1.place(relx = 0.5, rely = 0.2, anchor = 'c')

    entry2 = ctk.CTkEntry (app, width = 100, height = 30, border_width = 0,  corner_radius = 40, justify = 'c',
    fg_color = '#ffffff', bg_color = '#ffcc66', text_color = '#000066', font = ('Arial', 20, 'bold'))
    entry2.place(relx = 0.5, rely = 0.4, anchor = 'c')

    check1 = ctk.BooleanVar()
    check2 = ctk.BooleanVar()
    check3 = ctk.BooleanVar()
    check4 = ctk.BooleanVar()
    check5 = ctk.BooleanVar()

    box1 = ctk.CTkCheckBox (app, text = '1 2 3', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check1)
    box1.place(relx = 0.2, rely = 0.6, anchor = 'c')

    box2 = ctk.CTkCheckBox (app, text = 'a b c', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check2)
    box2.place(relx = 0.5, rely = 0.6, anchor = 'c')

    box3 = ctk.CTkCheckBox (app, text = 'A B C', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check3)
    box3.place(relx = 0.8, rely = 0.6, anchor = 'c')

    box4 = ctk.CTkCheckBox (app, text = '# % &', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check4)
    box4.place(relx = 0.25, rely = 0.7, anchor = 'c')

    box5 = ctk.CTkCheckBox (app, text = 'Убрать похожие\n(i,I,l,L,1,!,o,O,0)', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 25), variable = check5)
    box5.place(relx = 0.70, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (app, width = 300, height = 30, corner_radius = 20, text = 'Дальше', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command=lambda: check_input(int(check1.get()), int(check2.get()), int(check3.get()), int(check4.get()), int(check5.get()), entry1.get(), entry2.get()))
    button.place(relx = 0.5, rely = 0.9, anchor = 'c')

    button = ctk.CTkButton (app, width = 100, height = 30, corner_radius = 20, text = 'Выбрать все', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = lambda: select_all(box1, box2, box3, box4, box5))
    button.place(relx = 0.3, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (app, width = 100, height = 30, corner_radius = 20, text = 'Убрать все', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = lambda: deselect_all(box1, box2, box3, box4, box5))
    button.place(relx = 0.7, rely = 0.8, anchor = 'c')

label = ctk.CTkLabel (app, text = 'Приветствую тебя!', bg_color = '#ffcc66',
text_color = '#000000', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.1, anchor = 'c')

label = ctk.CTkLabel (app, text = 'Это генератор паролей', bg_color = '#ffcc66',
text_color = '#000000', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.25, anchor = 'c')

label = ctk.CTkLabel (app, text = 'Он поможет тебе\n надежно защитить\n твои аккаунты и данные', bg_color = '#ffcc66',
text_color = '#000000', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.45, anchor = 'c')

label = ctk.CTkLabel (app, text = 'И сделает это так\n как ты хочешь', bg_color = '#ffcc66',
text_color = '#000000', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.65, anchor = 'c')

button = ctk.CTkButton (app, width = 300, height = 70, corner_radius = 20, text = 'Отлично!', text_color = '#000000',
bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = filters)
button.place(relx = 0.5, rely = 0.85, anchor = 'c')

app.mainloop()
