from fbchat import Client
from fbchat.models import *


class Jarvis(object):
    def __init__(self, user_name, password, group_id):
        self.client = Client(user_name, password)
        self.group_id = group_id

    def send_message(self, message):
        self.client.send(Message(text=message), thread_id=self.group_id, thread_type=ThreadType.GROUP)
