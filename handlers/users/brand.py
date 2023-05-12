from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.users import brand_paginator_ikb, all_list_ikb
from keyboards.inline.users.general import UserCallbackData
from models.models import Asic
from parser.test_par import parse_and_save

user_brand_router = Router(name='user_brand')


@user_brand_router.callback_query(UserCallbackData.filter((F.target == 'brand') & (F.action == 'get')))
async def get_brand(callback: CallbackQuery, callback_data: UserCallbackData):
    if callback_data.videocard_id != 0 and callback_data.videocard_id != None:
        await callback.message.edit_text(
            text='Отлично, теперь ты точно знаешь, какое оборудование тебе необходимо. Перейдем к следующему шагу.'
        )
        await callback.message.answer(
            text='Нужен ли вам хостинг?',
            reply_markup=await brand_paginator_ikb(callback_data=callback_data)
        )
    elif callback_data.category_id == 1:

        parse_and_save()

        asics = await Asic.all()

        text = '\n\nASIC алгоритмы:\n'
        for asic in asics:
            text += f'/{asic.name} '

        await callback.message.edit_text(
            text=text.strip(),
            reply_markup=await all_list_ikb(callback_data=callback_data)
        )
        
    elif callback_data.category_id == 2:
        await callback.message.edit_text(
            text='Спасибо за ответ! К вам подключится специалист для обсуждения всех условий ☺',
        )
    else:
        await callback.message.edit_text(
            text='Нужен ли вам хостинг?',
            reply_markup=await brand_paginator_ikb(callback_data=callback_data)
        )

