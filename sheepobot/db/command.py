from .base import BaseModel
from peewee import TextField, IntegerField


class Command(BaseModel):
    name = TextField(index=True, unique=True)
    output = TextField()
    permissions_level = IntegerField()
    called = IntegerField()

    def call(self):
        self.called += 1
        self.save()
