from vkbottle import Bot
from config import api, labeler
from handlers import public_labeler


labeler.load(public_labeler)


bot = Bot(api=api,
          labeler=labeler)

bot.labeler.vbml_ignore_case = True


bot.run_forever()
