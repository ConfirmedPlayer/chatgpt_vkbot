from config import allowed_prefixes
from vkbottle.bot import Message
from vkbottle import BaseMiddleware


class CommandPrefixMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if not any(self.event.text[0] == prefix for prefix in allowed_prefixes):
            self.event.text = f'$STOP${self.event.text}'
            self.stop()
        else:
            self.event.text = self.event.text[1:]
