from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_panel = ReplyKeyboardMarkup(
    one_time_keyboard=False,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text='НАЖМИТЕ СЮДА 🏦'
            )
        ],
        # [
        #     KeyboardButton(
        #         text='КАЛЬКУЛЯТОР ДОХОДНОСТИ 🏦'
        #     )
        # ],
        # [
        #     KeyboardButton(
        #         text='ХОЧУ КУПИТЬ ОБОРУДОВАНИЕ 🏦'
        #     ),
        # ],
        # [
        #     KeyboardButton(
        #         text=' ИНДИВИДУАЛЬНАЯ КОНСУЛЬТАЦИЯ 🏦'
        #     )
        # ]
    ]
)
