COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'

FONT_VERY_LARGE = ('Constantia', 35, 'bold')
FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

BOX_PARAMS = {
    "fg_color": COLOR_DARK,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_WHITE,
    "border_color": COLOR_WHITE,
    "font": FONT_SMALL
}

ENTRY_PARAMS = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": FONT_SMALL
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": COLOR_WHITE,
    "button_hover_color": COLOR_LIME,
    "button_text_color": COLOR_BLACK
}

BTN_PARAMS = {
    "width": 50,
    "height": 40,
    "corner_radius": 50,
    "fg_color": COLOR_LIME,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_BLACK,
    "font": FONT_SMALL
}

MINI_BTN_PARAMS = {
    "width": 50,
    "height": 20,
    "corner_radius": 10,
    "fg_color": COLOR_WHITE,
    "hover_color": COLOR_LIME,
    "text_color": COLOR_BLACK,
    "font": FONT_SMALL
}

MESSAGE_LBL_PARAMS = {
    'text': '',
    'text_color': COLOR_LIME,
    'font': FONT_MEDIUM
}
MESSAGE_LBL_PLACE = {
    'relx': 0.5,
    'rely': 0.5,
    'anchor': 'c'
}

FINAL_LBL_PARAMS = {
    'text': 'Хотите повторить?',
    'text_color': COLOR_WHITE,
    'font':FONT_LARGE
}

FINAL_LBL_PLACE = {
    'relx': 0.5,
    'rely': 0.75,
    'anchor': 'c'
}

GREETINGS_PAGE_DATA = {
    'labels': [
        ('Приветствую тебя!', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.15),
        ('Это генератор паролей', COLOR_LIME, FONT_MEDIUM, 0.5, 0.3),
        ('Он поможет тебе', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.45),
        ('надежно защитить', COLOR_LIME, FONT_MEDIUM, 0.5, 0.6),
        ('твои аккаунты и данные!', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.75)
    ],
    'buttons': [
        ('Выйти', 'exit_app', 0.3, 0.9),
        ('Далее', 'start_app', 0.7, 0.9)
    ]
}

MAIN_PAGE_DATA = {
    'labels': [
        ('Сколько паролей\n нужно сгенерировать?', COLOR_LIME, FONT_MEDIUM, 0.5, 0.1),
        ('(Введите значение от 1 до 10)', COLOR_WHITE, FONT_SMALL, 0.5, 0.2),
        ('Необходимая длина пароля', COLOR_LIME, FONT_MEDIUM, 0.5, 0.35),
        ('(Введите значение от 5 до 20)', COLOR_WHITE, FONT_SMALL, 0.5, 0.4),
        ('Какие символы использовать?', COLOR_LIME, FONT_MEDIUM, 0.5, 0.55)
    ],
    'entrys': [
        ('count', 0.5, 0.27),
        ('length', 0.5, 0.48)
    ],
    'boxes': [
        ('digits', '1 2 3', 0.2, 0.65),
        ('lowercases', 'a b c', 0.5, 0.65),
        ('uppercases', 'A B C', 0.8, 0.65),
        ('symbols', '# % &', 0.35, 0.75),
        ('excludes', 'Убрать похожие\n(i,I,l,L,1,!,o,O,0)', 0.7, 0.75)
    ]
}

FINAL_PAGE_DATA = {
    'frames': [
        ('result_frame', 0, 0, 0.7, 0.7),
        ('button_frame', 0.7, 0, 0.3, 0.7)
    ],
    'buttons': [
        ('Не хочу', 'exit_app', 0.35, 0.9),
        ('Давай!', 'start_app', 0.65, 0.9)
    ]
}

DELAY_MESSAGES = {
    'waiting': [
        'Жду ответа от сервера...', 'Посылаю запрос...',
        'Нужно немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}

ERROR_MESSAGES = {
    'not_digit_count': {
        'message': 'В первом поле не введено число',
        'field': 'count'
    },
    'not_digit_length': {
        'message': 'Во втором поле не введено число',
        'field': 'length'
    },
    'too_low_count': {
        'message': 'Нужен хотя бы 1 пароль',
        'field': 'count'
    },
    'too_high_count': {
        'message': 'Допускается не больше 10 паролей',
        'field': 'count'
    },
    'too_low_length': {
        'message': 'Длина пароля не должна быть меньше 5 символов',
        'field': 'length'
    },
    'too_high_length': {
        'message': 'Допускается длина пароля не более 20 символов',
        'field': 'length'
    },
    'empty_boxes': {
        'message': 'Не выбран ни один вид символов',
        'field': 'box'
    }
}


