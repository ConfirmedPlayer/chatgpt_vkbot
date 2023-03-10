from vkbottle import API
from vkbottle.bot import BotLabeler
import os


token = os.environ['AI_VKBOT_TOKEN']
api = API(token)
labeler = BotLabeler()


openai_api_key = os.environ['CHATGPT_API_TOKEN']
openai_chat_model = 'gpt-3.5-turbo'
