from .base import BaseModel
from .command import Command
from peewee import TextField, ForeignKeyField


class Alias(BaseModel):
    name = TextField(index=True, unique=True)
    command = ForeignKeyField(Command, backref="aliases")
