from config import api
from vkbottle import BaseMiddleware, CtxStorage
from vkbottle.bot import Message
import time


class PreventFloodMiddleware(BaseMiddleware[Message]):
    storage = CtxStorage()
    flood_delay = 15
    flood_warning = 'Слишком частые запросы. Подождите {} сек.'

    async def pre(self):
        if self.event.peer_id not in self.storage:
            self.storage.set(self.event.peer_id, time.monotonic())
        else:
            last_message_time = self.storage.get(self.event.peer_id)
            difference_time = round(time.monotonic() - last_message_time)
            if difference_time <= self.flood_delay:
                seconds_left = self.flood_delay - difference_time
                await api.messages.send(peer_id=self.event.peer_id,
                                        message=self.flood_warning.format(seconds_left),
                                        random_id=0)
                self.stop()
            else:
                self.storage.delete(self.event.peer_id)
