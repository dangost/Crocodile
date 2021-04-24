from models.client import Client
from datetime import datetime


class Log:
    def __init__(self, client: Client, message: str = None):
        self.client = client
        self.message = message

    @property
    def __current_date(self):
        current_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return current_date

    def __str__(self):
        if self.message is None:
            log = f"{self.__current_date} | {self.client.address} | {self.client.name} join chat"
        else:
            log = f"{self.__current_date} | {self.client.address} | {self.client.name}: {self.message}"
        return log
