import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
import string


class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
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
                **cfg.BTN_PARAMS_1
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
                anchor='c'
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
            **cfg.BTN_PARAMS_1
        )
        button.place(
            relx=0.5,
            rely=0.9,
            anchor='c'
        )

    def update_ui(self):
        for name in self.entrys:
            self.entrys[name].delete(0, 'end')

        for name in self.variables:
            self.variables[name].set(False)

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

            if status in [
                'not_digit_count',
                'too_low_count',
                'too_high_count'
            ]:
                self.wait_window(error_message)
                self.entrys['count'].delete(0, 'end')
                self.entrys['count'].focus_force()
                return

            if status in [
                'not_digit_length',
                'too_low_length',
                'too_high_length'
            ]:
                self.wait_window(error_message)
                self.entrys['length'].delete(0, 'end')
                self.entrys['length'].focus_force()
                return

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
        self.widgets = []

        frame_data = [
            ('result', 0, 0.7),
            ('copy', 0.7, 0.3)
        ]

        for name, relx, relwidth in frame_data:
            frame = ctk.CTkFrame(
                self,
                fg_color=cfg.FRM_COLOR
            )

            frame.place(
                relx=relx,
                rely=0,
                relwidth=relwidth,
                relheight=0.7
            )

            self.frames[name] = frame

        label = ctk.CTkLabel(
            self,
            text='Хотите повторить?',
            text_color=cfg.TXT_COLOR_2,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.75,
            anchor='c'
        )

        button_data = [
            ('Не хочу', self.controller.exit_app),
            ('Давай!', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS_1
            )
            button.place(
                relx=0.3 + (idx * 0.4),
                rely=0.9,
                anchor='c'
            )

    def get_result(self, passwords):
        for key in passwords:
            label = ctk.CTkLabel(
                self.frames['result'],
                text=key,
                text_color=cfg.TXT_COLOR_1,
                font=cfg.LIT_FONT
            )

            label.pack(
                side='top',
                expand=True,
                fill='both'
            )

            button = ctk.CTkButton(
                self.frames['copy'],
                text='copy',
                command=lambda k=key: copy(k),
                **cfg.BTN_PARAMS_2
            )

            button.pack(
                side='top',
                expand=True
            )

            self.widgets.append(label)
            self.widgets.append(button)

    def update_ui(self):
        for widget in self.widgets:
            widget.destroy()

        self.widgets.clear()


class MainLogic:
    def check_input(self, user_input):
        if not user_input['count'].isdigit():
            return 'not_digit_count'

        if not user_input['length'].isdigit():
            return 'not_digit_length'

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
        for page_class in (GreetingsPage, MainPage, MessagePage, FinalPage):
            page_name = page_class.__name__
            self.pages[page_name] = page_class(
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
        self.pages['FinalPage'].update_ui()
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