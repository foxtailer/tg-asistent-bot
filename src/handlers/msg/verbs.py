import random

from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from src.states.user_states import UserState


verbs_msg_router = Router()


@verbs_msg_router.message(UserState.verbs)
async def verbs_msg(msg: types.Message, state: FSMContext, bot):
    data = await state.get_data()
    data = data['verbs']
    print(data)

#    while True:
    form = random.choice(["V2 (Past simple)",
                          "V3 (Past participle)"])

    #await msg.reply(f"{form} of {V1[start]}")

    if msg.text.lower().strip() == data['v2'][0]:
        await msg.reply('++')        
    else:
        await msg.reply('--')
        await msg.delete()

