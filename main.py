import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
import string

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
            ('Вперёд!', self.controller.create_game)
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
            ('count', 0.27),
            ('length', 0.48)
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
            ('lowercases', 'a b c', 0.5, 0.65),
            ('uppercases', 'A B C', 0.8, 0.65),
            ('symbols', '# % &', 0.35, 0.75),
            (
                'excludes',
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
            command=self.send_input,
            **cfg.BTN_PARAMS
        )
        button.place(
            relx=0.5,
            rely=0.9,
            anchor='c'
        )

    def update_ui(self):
        self.clear_count_entry
        self.entrys['count'].insert(0, '3')

        self.clear_length_entry
        self.entrys['length'].insert(0, '15')

        for name, var in self.variables.items():
            var.set(name not in ['symbols', 'excludes'])

    def clear_count_entry(self):
        self.entrys['count'].delete(0, 'end')
        self.entrys['count'].focus_set()

    def clear_length_entry(self):
        self.entrys['length'].delete(0, 'end')
        self.entrys['length'].focus_set()

    def send_input(self):
        user_input = {
            'count': self.entrys['count'].get(),
            'length': self.entrys['length'].get(),
            'digits': self.variables['digits'].get(),
            'lowercases': self.variables['lowercases'].get(),
            'uppercases': self.variables['uppercases'].get(),
            'symbols': self.variables['symbols'].get(),
            'excludes': self.variables['excludes'].get()
        }

        self.controller.transfer_data(user_input)

    def give_feedback(self, status, passwords):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )
            return

        self.controller.transfer_final_data(passwords)


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

    def change_message(self, status):
        self.message_label.configure(
            text=choice(cfg.APP_MESSAGES[status])
        )

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        self.frames = {}

        frame_data = [
            ('result', 0, 0.3, 0.7),
            ('copy', 0, 0.3, 0.7)
        ]

        for name, coord_1, coord_2, coord_3:


        self.result_frame = ctk.CTkFrame(
            self,
            fg_color=cfg.FRM_COLOR
        )

        self.result_frame.place(
            relx=0,
            rely=0,
            relwidth=0.7,
            relheight=0.7
        )

        self.copy_frame = ctk.CTkFrame(
            self,
            fg_color=cfg.FRM_COLOR
        )

        self.copy_frame.place(
            relx=0.7,
            rely=0,
            relwidth=0.3,
            relheight=0.7
        )

        label = ctk.CTkLabel(
            self,
            text='Хотите повторить?',
            text_color=cfg.TXT_COLOR_1,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.75,
            anchor='c'
        )

    def get_result(self, passwords):
        for key in passwords:
            label = ctk.CTkLabel(
                self.result_frame,
                text=key,
                text_color=cfg.TXT_COLOR_2,
                font=cfg.LIT_FONT
            )

            label.pack(
                side='top',
                expand=True,
                fill='both'
            )

            button = ctk.CTkButton(
                self.copy_frame,
                text='copy',
                #command=lambda l = label.cget('text'): copy(l),
                command=lambda k=key: copy(k),
                **cfg.BTN_PARAMS_2
            )

            button.pack(
                side='top',
                expand=True
            )





class MainLogic:
    def check_input(self, user_input):
        if (not user_input['count'].isdigit() or
        not user_input['length'].isdigit()):
            return 'not_digit'

        count = int(user_input['count'])
        length = int(user_input['length'])

        if count == 0:
            return 'too_low_count'
        if count > 10:
            return 'too_high_count'
        if length < 5:
            return 'too_low_length'
        if length > 20:
            return 'too_high_length'

        keys = ['digits', 'lowercases', 'uppercases', 'symbols']

        if not any(user_input[key] for key in keys):
            return 'empty_boxes'

        return None

    def generate(self, user_input):
        error_status = self.check_input(user_input)
        if error_status:
            return error_status, []

        pool = ''
        if user_input['digits']:
            pool += string.digits
        if user_input['lowercases']:
            pool += string.ascii_lowercase
        if user_input['uppercases']:
            pool += string.ascii_uppercase
        if user_input['symbols']:
            pool += "#%&@$^*!?+=-"

        if user_input['excludes']:
            bad_chars = "iIlL1!oO0"
            clean_pool = ""

            for char in pool:
                if char not in bad_chars:
                    clean_pool += char

            pool = clean_pool

        passwords = []
        count = int(user_input['count'])
        length = int(user_input['length'])

        for _ in range(count):
            password = "".join(choice(pool) for _ in range(length))
            passwords.append(password)

        return 'success', passwords


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Генератор паролей')
        self.geometry('400x500+900+300')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()

        self.pages = {}
        self.current_frame = None
        for F in (GreetingsPage, MainPage, MessagePage, FinalPage):
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
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def create_game(self):
        self.pages['MessagePage'].change_message('loading')
        self.switch_to('MessagePage')
        self.pages['MainPage'].update_ui()
        self.after(3000, lambda: self.switch_to("MainPage"))

    def transfer_data(self, user_input):
        status, passwords = self.main_logic.generate(user_input)
        self.pages['MainPage'].give_feedback(status, passwords)

    def transfer_final_data(self, passwords):
        self.pages['MessagePage'].change_message('waiting')
        self.switch_to('MessagePage')
        self.pages['FinalPage'].get_result(passwords)
        self.after(3000, lambda: self.switch_to('FinalPage'))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()





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