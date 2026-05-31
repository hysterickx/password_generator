import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg

class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Приветствую тебя!', cfg.TXT_COLOR_1),
            ('Это генератор паролей', cfg.TXT_COLOR_2),
            ('Он поможет тебе', cfg.TXT_COLOR_1),
            ('надежно защитить', cfg.TXT_COLOR_2),
            ('твои аккаунты и данные!', cfg.TXT_COLOR_1)
        ]

        for idx, (text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=cfg.BIG_FONT
            )
            label.place(
                relx=0.5,
                rely=0.15 + (idx * 0.13),
                anchor='c'
            )

        button_data = [
            ('Выйти', self.controller.exit_app),
            ('Вперёд!', lambda: self.controller.switch_to('MainPage'))
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=0.3 + (idx * 0.4),
                rely=0.85,
                anchor='c'
            )

class MainPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        txt = cfg.APP_MESSAGES['lbl_txt']

        label_data = [
            (txt[0], 0.1,  cfg.TXT_COLOR_1, cfg.MID_FONT),
            (txt[1], 0.18, cfg.TXT_COLOR_2, cfg.LIT_FONT),
            (txt[2], 0.35, cfg.TXT_COLOR_1, cfg.MID_FONT),
            (txt[3], 0.4,  cfg.TXT_COLOR_2, cfg.LIT_FONT),
            (txt[4], 0.57, cfg.TXT_COLOR_1, cfg.MID_FONT)
        ]

        for text, rely, color, font in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )

            label.place(
                relx=0.5,
                rely=rely,
                anchor = 'c'
            )

        self.entrys = {}

        entry_data = [
            ('count_entry', 0.27),
            ('lenght_entry', 0.48)
        ]

        for name, rely in entry_data:
            entry = ctk.CTkEntry(
                self,
                **cfg.ENTRY_PARAMS
            )

            entry.place(
                relx=0.5,
                rely=rely,
                anchor='c'
            )

            self.entrys[name] = entry


        self.variables = {}
        self.boxes = {}

        box_data = [
            ('digits', '1 2 3', 0.2, 0.65),
            ('lowercase', 'a b c', 0.5, 0.65),
            ('uppercase', 'A B C', 0.8, 0.65),
            ('symbols', '# % &', 0.35, 0.75),
            (
                'exclude',
                'Убрать похожие\n(i,I,l,L,1,!,o,O,0)',
                0.7, 0.75
            )
        ]

        for key, text, relx, rely in box_data:
            self.variables[key] = ctk.BooleanVar(value=False)

            box = ctk.CTkCheckBox(
                self,
                text=text,
                variable=self.variables[key],
                **cfg.BOX_PARAMS
            )
            box.place(
                relx=relx,
                rely=rely,
                anchor='c'
            )

            self.boxes[key] = box

        button = ctk.CTkButton(
            self,
            text='Готово!',
            command=lambda: print('sss'),
            **cfg.BTN_PARAMS
        )
        button.place(
            relx=0.5,
            rely=0.9,
            anchor='c'
        )


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        self.message_label = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.TXT_COLOR_1,
            font=cfg.BIG_FONT
        )
        self.message_label.place(
            relx=0.5,
            rely=0.5,
            anchor='c'
        )

    def change_text(self, status):
        self.message_label.configure(
            text=choice(cfg.APP_MESSAGES[status])
        )

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Генератор паролей')
        self.geometry('400x500+900+300')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.pages = {}
        self.current_frame = None
        for F in (GreetingsPage, MainPage, MessagePage):
            page_name = F.__name__
            self.pages[page_name] = F(
                master=self.main_frame,
                controller=self
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def exit_app(self):
        self.pages['MessagePage'].change_text('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()



#digits = '0123456789'
#lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
#uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#punctuation = '!#$%&*+-=?@^_'
#waitings = ['Мне нужно\n несколько секундочек...', 'Дайте мне\n немножечко времени...', 'Почти готово...', 'Секундочку...']
#
#def clear_all():
#    for widget in app.winfo_children():
#        widget.destroy()
#
#def select_all(box1, box2, box3, box4, box5):
#    for check in [box1, box2, box3, box4, box5]:
#        check.select()
#
#def deselect_all(box1, box2, box3, box4, box5):
#    for check in [box1, box2, box3, box4, box5]:
#        check.deselect()
#
#def end():
#    clear_all()
#    label = ctk.CTkLabel (app, text = 'До новых встреч!', bg_color = '#ffcc66',
#    text_color = '#000000', font = ('Arial', 23, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#    app.after(5000, app.destroy)
#
#def repeat():
#    clear_all()
#    label = ctk.CTkLabel (app, text = 'Запускаю процесс...', bg_color = '#ffcc66',
#    text_color = '#000000', font = ('Arial', 23, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#    app.after(5000, filters)
#
#def result(passwords):
#    clear_all()
#    frame1 = ctk.CTkFrame(app, bg_color = '#ffcc66', fg_color = '#ffcc66')
#    frame1.place(relx = 0, rely = 0, relwidth = 0.7, relheight = 0.7)
#
#    frame2 = ctk.CTkFrame(app, bg_color = '#ffcc66', fg_color = '#ffcc66')
#    frame2.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 0.7)
#
#    def copy_all():
#        copy (passwords)
#        button2.configure (text = 'Скопировано', text_color_disabled = '#000000', state = 'disabled', fg_color = '#ffff99')
#        button2.after(1000, lambda: button2.configure(text = 'Copy all', state = 'normal', fg_color = '#ffffff', text_color = '#000000'))
#
#    def copy_action (text, button):
#        copy(text)
#        button.configure (text = '✅', text_color_disabled = '#000000', state = 'disabled', fg_color = '#ffff99')
#        button.after(1000, lambda: button.configure(text = 'Copy', state = 'normal', fg_color = '#ffffff', text_color = '#000000'))
#
#    for i in passwords:
#        label = ctk.CTkLabel (frame1, text = i, bg_color = '#ffcc66',
#        text_color = '#000000', font = ('Arial', 23, 'bold'))
#        label.pack(side = 'top', expand = True, fill = 'both')
#
#        button = ctk.CTkButton (frame2, width = 120, height = 30, text = 'Copy', bg_color = '#ffcc66', fg_color = '#ffffff',
#        hover_color = '#996633', corner_radius = 40,  text_color = '#000000', font = ('Arial', 18, 'bold'))
#        button.configure(command = lambda text = i, but = button: copy_action(text, but))
#        button.pack(side = 'top', expand = True)
#
#    button2 = ctk.CTkButton (app, width = 200, height = 30, corner_radius = 20, text = 'Copy all', text_color = '#000000',
#    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = copy_all)
#    button2.place(relx = 0.5, rely = 0.75, anchor = 'c')
#
#    label2 = ctk.CTkLabel (app, text = 'Хотите повторить?', bg_color = '#ffcc66',
#    text_color = '#000000', font = ('Arial', 23, 'bold'))
#    label2.place(relx = 0.5, rely = 0.85, anchor = 'c')
#
#    button3 = ctk.CTkButton (app, width = 100, height = 50, corner_radius = 40, text = 'Да', text_color = '#000000',
#    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = repeat)
#    button3.place(relx = 0.35, rely = 0.95, anchor = 'c')
#
#    button4 = ctk.CTkButton (app, width = 100, height = 50, corner_radius = 40, text = 'Нет', text_color = '#000000',
#    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = end)
#    button4.place(relx = 0.65, rely = 0.95, anchor = 'c')
#
#def create(check1, check2, check3, check4, check5, count, lenght):
#    clear_all()
#
#    chars = ''
#    symbols = [digits, lowercase_letters, uppercase_letters, punctuation]
#    passwords = []
#    value = 0
#
#    for i in [check1, check2, check3, check4]:
#        if i == 1:
#            chars += symbols[value]
#        value += 1
#
#    if check5 == 1:
#         for j in 'i, I, l, L, 1, !, o, O, 0':
#            if j in chars:
#                chars = chars.replace(j, '')
#
#    for k in range (count):
#        password = ''
#        for m in range (lenght):
#            password += choice(chars)
#        passwords.append(password)
#
#    label = ctk.CTkLabel (app, text = choice(waitings), bg_color = '#ffcc66',
#    text_color = '#000000', font = ('Arial', 30, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#    app.after (5000, lambda: result(passwords))
#
#def check_input(check1, check2, check3, check4, check5, count, lenght):
#    value = 0
#    for i in [check1, check2, check3, check4]:
#        if i == 0:
#            value += 1
#    if value == 4:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Не выбран ни один тип символов'
#        )
#    elif len(count) == 0 or len(lenght) == 0:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Не все значения введены'
#        )
#    elif count.isdigit() == False or lenght.isdigit() == False:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Для ввода допускаются только циферки'
#        )
#    elif int(count) < 1:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Нужен хотя бы 1 пароль'
#        )
#    elif int(lenght) < 5:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Недостаточная длина пароля'
#        )
#    elif int(count) > 10:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Слишком много паролей'
#        )
#    elif int(lenght) > 20:
#        CTkMessagebox(
#            app,
#            **cfg.MSG_PARAMS,
#            message='Слишком длинный пароль'
#        )
#    else:
#        create(check1, check2, check3, check4, check5, int(count), int(lenght))
#
