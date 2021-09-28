from .base import BaseModel
from peewee import TextField, IntegerField

from sheepobot.enums import PermissionsLevel


class Command(BaseModel):
    name = TextField(index=True, unique=True)
    output = TextField()
    permissions_level = IntegerField(default=PermissionsLevel.USER)
    called = IntegerField(default=0)

    def call(self):
        self.called += 1
        self.save()
