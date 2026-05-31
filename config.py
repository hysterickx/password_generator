FRM_COLOR = '#0d0a0c'
TXT_COLOR_1 = '#99ff66'
TXT_COLOR_2 = '#ffffff'
TXT_COLOR_3 = '#000000'
BTN_COLOR_1 = '#99ff66'
BTN_COLOR_2 = '#ffffff'
BTN_COLOR_3 = '#000000'

BIG_FONT = ('Constantia', 27)
MID_FONT = ('Constantia', 25)
LIT_FONT = ('Constantia', 20)


BOX_PARAMS = {
    "fg_color": FRM_COLOR,
    "hover_color": TXT_COLOR_2,
    "text_color": TXT_COLOR_2,
    "border_color": TXT_COLOR_2,
    "font": LIT_FONT
}

ENTRY_PARAMS = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": ('Arial', 20, 'bold')
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": BTN_COLOR_2,
    "button_hover_color": BTN_COLOR_1,
    "button_text_color": BTN_COLOR_3
}

BTN_PARAMS = {
    "width": 50,
    "height": 40,
    "corner_radius": 50,
    "fg_color": BTN_COLOR_1,
    "hover_color": BTN_COLOR_2,
    "text_color": BTN_COLOR_3,
    "font": ('Constantia', 20)
}

APP_MESSAGES = {
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
    ],
    'lbl_txt': [
        'Сколько паролей\n нужно сгенерировать?',
        '(Введите значение от 1 до 10)',
        'Необходимая длина пароля',
        '(Введите значение от 5 до 20)',
        'Какие символы использовать?'
    ]
}