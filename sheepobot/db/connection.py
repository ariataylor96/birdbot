from sheepobot import env
from peewee import SqliteDatabase

connection: SqliteDatabase = SqliteDatabase(env("DATABASE_PATH", default="/code/data.db"))
