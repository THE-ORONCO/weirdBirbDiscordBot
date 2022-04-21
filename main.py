#!/usr/bin/env python3
"""
This script starts the bot.
"""
import os
import discord
from dotenv import dotenv_values

from bots.weirdbirbbot import WeirdBirbBot

if __name__ == '__main__':
    config = dotenv_values('.env')
    cogs_dir = config['COGS_DIR']
    command_prefix = config['PREFIX']
    intents = discord.Intents.all()

    bot = WeirdBirbBot(command_prefix=command_prefix, intents=intents)

    cogs = os.listdir('./cogs')
    for cog in [f'{cogs_dir}.{cog[:-len(".py")]}' for cog in os.listdir(cogs_dir) if
                cog.endswith('.py') and '__init__' not in cog]:
        try:
            bot.load_extension(cog)
            print(f'loaded: {cog}')
        except discord.ExtensionNotFound as e:
            print(f'no extension in {cog} please remove from cog directory')
        except discord.ExtensionAlreadyLoaded as e:
            print(f'no extension in {cog} already loaded')
        except discord.ExtensionFailed as e:
            print(f'extension in {cog} was bad')
        except discord.NoEntryPointError as e:
            print(f'extension in {cog} is missing a setup entry point function')

    bot.run(config['TOKEN'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
