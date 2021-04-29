from abc import ABC, abstractmethod
from typing import List

from application.entities.lobbies.model import Lobby
from application.entities.users.model import User


class BaseDatabase(ABC):
    # entities
    users: List[User]
    lobbies: List[Lobby]

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass
