from config import api, labeler
from handlers import public_labeler
from middlewares.command_prefix import CommandPrefixMiddleware
from vkbottle import Bot


labeler.load(public_labeler)


bot = Bot(api=api, labeler=labeler)

bot.labeler.vbml_ignore_case = True

bot.labeler.message_view.register_middleware(CommandPrefixMiddleware)


bot.run_forever()
