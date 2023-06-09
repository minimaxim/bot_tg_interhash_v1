from aiogram import Router, F
from aiogram.filters import state
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.formilize import Form
from keyboards.inline.users import brand_paginator_ikb, all_list_ikb, cur_ikb
from keyboards.inline.users.general import UserCallbackData
from keyboards.reply.users import walet_panel
from parser.connection import connect_to_db

user_brand_router = Router(name='user_brand')


@user_brand_router.callback_query(UserCallbackData.filter((F.target == 'brand') & (F.action == 'get')))
async def get_brand(callback: CallbackQuery, callback_data: UserCallbackData, state: FSMContext) -> None:

    connect_to_db()

    user = callback.from_user.id
    category = callback_data.category_id

    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""SELECT name FROM categories WHERE id = (%s)""", (category,))
    category_name = cur.fetchall()[0][0]
    conn.commit()

    cur.execute(f"""UPDATE users SET category_name = (%s) WHERE id = (%s)""", (category_name, user))
    conn.commit()

    cur.close()
    conn.close()

    if callback_data.category_id == 1:

        await state.set_state(Form.coin)
        await callback.message.edit_text(
            text='Выберите валюту для рассчета',
            reply_markup=await cur_ikb()
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


