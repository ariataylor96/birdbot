import discord
from sheepobot import env, db

from sheepobot.parsing import Message

client: discord.Client = discord.Client()


@client.event
async def on_ready() -> None:
    print("Ret-2-go!")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return

    parsed: Message = Message(message)
    print(parsed.raw.author.roles)


def main() -> None:
    client.run(env.str("DISCORD_BOT_TOKEN"))
