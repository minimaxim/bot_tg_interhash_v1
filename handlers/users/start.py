from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboards.inline.users import start_ikb
from keyboards.inline.users.general import UserCallbackData


user_start_router = Router(name='user_start')


@user_start_router.message(F.text == 'НАЖМИТЕ СЮДА 🏦')
async def send_start_ikb(message: Message):
    await message.delete()
    await message.answer(
        text='👋 Привет, '
             
             'Мы компания Interhash, Занимаемся предоставлением комплексных услуг для майнинга. Мы на рынке с 2017 года и являемся официальным представителями майнинг-пула ViaBTC в Европе и странах СНГ.',
        reply_markup=await start_ikb()
    )


@user_start_router.callback_query(UserCallbackData.filter(F.action == 'all'))
async def start_panel(callback: CallbackQuery):
    await callback.message.edit_text(
        text='👋 Привет, '

             'Мы компания Interhash, Занимаемся предоставлением комплексных услуг для майнинга. Мы на рынке с 2017 года и являемся официальным представителями майнинг-пула ViaBTC в Европе и странах СНГ.',
        reply_markup=await start_ikb()
    )
