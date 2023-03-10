from config import openai_api_key, openai_chat_model
from middlewares.prevent_flood import PreventFloodMiddleware
from vkbottle.bot import BotLabeler, Message
import openai


openai.api_key = openai_api_key


public_labeler = BotLabeler()
public_labeler.message_view.register_middleware(PreventFloodMiddleware)


@public_labeler.message(text='ии <text>')
async def chatgpt_prompt(message: Message, text: str):
    completion = await openai.ChatCompletion.acreate(model=openai_chat_model,
                                                     messages=[{'role': 'user',
                                                                'content': text}])
    await message.reply(completion.choices[0].message.content)
