from .connection import connection
from .command import Command
from .alias import Alias

connection.connect()
connection.create_tables([Command, Alias])
