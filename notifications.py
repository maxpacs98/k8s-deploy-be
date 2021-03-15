from abc import abstractmethod, ABC
from functools import cached_property
from typing import Dict

from vonage import Client


class AbstractNotificator(ABC):
    def __init__(self, config: Dict):
        self._config = config

    @abstractmethod
    def notify(self, sender: str, receiver: str, **data):
        pass


class SmsNotificator(AbstractNotificator):
    def __init__(self, config: Dict):
        super().__init__(config)

    def notify(self, sender: str, receiver: str, **data):
        self.client.send_message({'from': sender, 'to': receiver, **data})

    @cached_property
    def client(self):
        return Client(**self._config)
