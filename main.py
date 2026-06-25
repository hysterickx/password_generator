import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from functools import partial
import string


class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        label_data = cfg.GREETINGS_PAGE_DATA['labels']
        button_data = cfg.GREETINGS_PAGE_DATA['buttons']

        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')

        for text, command_arg, relx, rely in button_data:
            button = ctk.CTkButton(
                self, text=text,
                command=partial(
                    controller.handle_command, command_arg
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')


class MainPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        label_data = cfg.MAIN_PAGE_DATA['labels']

        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx,rely=rely,anchor='c')

        self.entrys = {}
        entry_data = cfg.MAIN_PAGE_DATA['entrys']

        for name, relx, rely in entry_data:
            entry = ctk.CTkEntry(
                self,
                **cfg.ENTRY_PARAMS
            )
            entry.place(relx=relx, rely=rely,anchor='c')
            self.entrys[name] = entry

        self.variables = {}
        box_data = cfg.MAIN_PAGE_DATA['boxes']

        for key, text, relx, rely in box_data:
            self.variables[key] = ctk.BooleanVar(value=False)
            box = ctk.CTkCheckBox(
                self,
                text=text,
                variable=self.variables[key],
                **cfg.BOX_PARAMS
            )
            box.place(relx=relx, rely=rely, anchor='c')

        button = ctk.CTkButton(
            self,
            text='Готово!',
            command=self.send_data,
            **cfg.BTN_PARAMS
        )
        button.place(relx=0.5, rely=0.9, anchor='c')

    def send_data(self):
        user_input = {}

        for key, entry in self.entrys.items():
            user_input[key] = entry.get()

        for key, var in self.variables.items():
            user_input[key] = var.get()

        self.controller.handle_command(
            'transfer_data', user_input
        )

    def show_entry_message(self, status, entry_key):
        text = cfg.ERROR_MESSAGES[status]['message']
        error_message = CTkMessagebox(
            app,
            message=text,
            **cfg.MSG_PARAMS
        )
        self.wait_window(error_message)
        self.entrys[entry_key].delete(0, 'end')
        self.entrys[entry_key].focus()

    def show_box_message(self, status):
        text = cfg.ERROR_MESSAGES[status]['message']
        error_message = CTkMessagebox(
            app,
            message=text,
            **cfg.MSG_PARAMS
        )

    def update_ui(self):
        for name in self.entrys:
            self.entrys[name].delete(0, 'end')
        for name in self.variables:
            self.variables[name].set(False)


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.label = ctk.CTkLabel(
            self,
            **cfg.MESSAGE_LBL_PARAMS
        )
        self.label.place(**cfg.MESSAGE_LBL_PLACE)

    def change_message(self, stage):
        self.label.configure(
            text=choice(cfg.DELAY_MESSAGES[stage])
        )


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.frames = {}
        self.widgets = []
        frame_data = cfg.FINAL_PAGE_DATA['frames']

        for name, relx, rely, relwidth, relheight in frame_data:
            frame = ctk.CTkFrame(
                self,
                fg_color=cfg.COLOR_DARK
            )
            frame.place(
                relx=relx,
                rely=rely,
                relwidth=relwidth,
                relheight=relheight
            )
            self.frames[name] = frame

        label = ctk.CTkLabel(
            self,
            **cfg.FINAL_LBL_PARAMS
        )
        label.place(**cfg.FINAL_LBL_PLACE)

        button_data = cfg.FINAL_PAGE_DATA['buttons']

        for text, command_arg, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(
                    controller.handle_command, command_arg
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def show_result(self, passwords):
        for key in passwords:
            label = ctk.CTkLabel(
                self.frames['result_frame'],
                text=key,
                text_color=cfg.COLOR_LIME,
                font=cfg.FONT_SMALL
            )
            label.pack(side='top', expand=True, fill='both')

            button = ctk.CTkButton(
                self.frames['button_frame'],
                text='copy',
                command=partial(copy, key),
                **cfg.MINI_BTN_PARAMS
            )
            button.pack(side='top', expand=True)

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

        keys = [
            'digits', 'lowercases',
            'uppercases', 'symbols'
        ]

        if not any(user_input[key] for key in keys):
            return 'empty_boxes'

        return None

    def create_passwords(self, user_input):
        error_status = self.check_input(user_input)
        if error_status:
            return error_status

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
            bad_chars = "iIlL1!oO0j"
            clean_pool = ""

            for char in pool:
                if char not in bad_chars:
                    clean_pool += char

            pool = clean_pool

        passwords = []
        count = int(user_input['count'])
        length = int(user_input['length'])

        for _ in range(count):
            password = "".join(
                choice(pool) for _ in range(length)
            )
            passwords.append(password)

        return passwords


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
        page_types = [
            ("GreetingsPage", GreetingsPage),
            ("MainPage", MainPage),
            ("FinalPage", FinalPage),
            ("MessagePage", MessagePage)
        ]

        for page_name, page_class in page_types:
            self.pages[page_name] = page_class(
                self.main_frame, self
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def transfer_data(self, user_input):
        result = self.main_logic.create_passwords(user_input)

        if isinstance(result, str):
            entry_key = cfg.ERROR_MESSAGES[result]['field']
            if entry_key in ('count', 'length'):
                self.pages['MainPage'].show_entry_message(
                    result, entry_key
                )
            else:
                self.pages['MainPage'].show_box_message(
                    result
                )
        else:
            self.send_result(result)

    def send_result(self, passwords):
        self.pages['MessagePage'].change_message('waiting')
        self.switch_to('MessagePage')
        self.pages['FinalPage'].show_result(passwords)
        self.after(3000, lambda: self.switch_to('FinalPage'))

    def handle_command(self, target, *args):
        if hasattr(self, target):
            method = getattr(self, target)
            if callable(method):
                method(*args)
                return
        self.switch_to(target)

    def exit_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def start_app(self):
        self.pages['MessagePage'].change_message('loading')
        self.switch_to('MessagePage')
        self.pages['MainPage'].update_ui()
        self.pages['FinalPage'].update_ui()
        self.after(3000, lambda: self.switch_to("MainPage"))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()