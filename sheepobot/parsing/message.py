from discord import Message

from sheepobot.db import Command, Alias
from sheepobot.enums import PermissionsLevel

from peewee import DoesNotExist
from typing import Optional

from contextlib import suppress
import shlex


class Message:
    command: str
    args: list[str]
    body: str
    raw: Message
    author_permissions: PermissionsLevel

    def __init__(self, m: Message):
        parts: list[str] = []
        try:
            parts = shlex.split(m.content)
        except ValueError:
            # Not valid shell format, just split on whitespace instead
            parts = m.content.split(" ")

        # Case-insensitive commands
        command: str = parts[0].lower()
        if command.startswith("!"):
            command = command[1:]

        self.command = command
        self.args = parts[1:]
        self.body = m.content[len(command) + 1 :]
        self.raw = m

        author_roles = [r.name.lower() for r in m.author.roles]
        self.author_permissions = (
            PermissionsLevel.MOD if "runner" in author_roles else PermissionsLevel.USER
        )

    @property
    def matching_command(self) -> Optional[Command]:
        with suppress(DoesNotExist):
            return Command.get(Command.name == self.command)

        with suppress(DoesNotExist):
            return Alias.get(Alias.name == self.command).command
