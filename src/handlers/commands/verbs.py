import random

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.states.user_states import UserState
from src.services.variables import V1, V2, V3, V2_sentences, V3_sentences


verbs_router = Router()


@verbs_router.message(Command("verbs"))
async def verbs_play(msg: types.Message, command, state: FSMContext):
    await state.set_state(UserState.verbs)
    data = {
            'flag': False,
            'corect': None,
            'weigts': None,
            'score': None,
            'indexes': None,
            }

    if command.args:
        args = command.args.replace(' ', '')
        args = tuple(int(i) for i in command.args.strip().lower().split('-'))
        
        if len(args) == 2 and all(isinstance(i, int) for i in args):
            start, stop = args

            if 0 <= start < stop <= 155:
                data['v1'] = V1[start:stop]
                data['v2'] = V2[start:stop]
                data['v3'] = V3[start:stop]
                data['v2s'] = V2_sentences[start:stop]
                data['v3s'] = V3_sentences[start:stop]
                indexes = list(range(stop - start))
                random.shuffle(indexes)
                data['indexes'] = indexes
                data['correct'] = V2[start]
                
                await state.update_data(verbs=data)

                await msg.reply(f"V2 (Past simple) of {V1[start]}")
            else:
                await msg.reply("Bad arguments")
        else:
            await msg.reply("Bad arguments")
    else:
        await msg.reply("Require arguments: int-int")
    
    await msg.delete()
