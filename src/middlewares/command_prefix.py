from vkbottle.bot import Message
from vkbottle import BaseMiddleware


class CommandPrefixMiddleware(BaseMiddleware[Message]):
    prefixes = ('/', '!', '$')

    async def pre(self):
        if not any(self.event.text[0] == prefix for prefix in self.prefixes):
            self.stop()
        else:
            self.event.text = self.event.text[1:]
