from typing import Final
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from modules.diccionario_rae import get_rae_results
from modules.help import show_help

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="j!", intents=intents)
bot.help_command = None # Disable built-in help command

# Handle global errors
@bot.event
async def on_command_error(ctx, error):
    def send_error_embed(title: str, description: str):
        """Helper function to send an error embed."""
        embedded_error = discord.Embed(title=title, description=description, color=0xFF5733)
        return ctx.send(embed=embedded_error)

    if isinstance(error, commands.CommandNotFound):
        await send_error_embed("Invalid command", f'Command not found. Type `j!help` for more info.')
        await send_error_embed("Comando inválido", f'Comando no encontrado. Escriba `j!help` para más información.')

    elif isinstance(error, commands.MissingRequiredArgument):
        # Ensure we're handling the right command (rae in this case)
        if ctx.command.name == "rae":
            await send_error_embed("Missing argument",
                                    f'The command `{ctx.command.name}` requires additional arguments. Example usage: `j!rae libro`. Type `j!help` for more info.')
            await send_error_embed("Argumento faltante",
                                   f'El comando `{ctx.command.name}` requiere argumentos adicionales. Ejemplo de uso: `j!rae libro`. Escriba `j!help` para más información.')

    elif isinstance(error, commands.BadArgument):
        await send_error_embed("Invalid argument", f'The argument for the command is not valid. Type `j!help` for more info.')
        await send_error_embed("Argumento inválido", f'El argumento del comando no es válido. Escriba `j!help` para más información.')

    else:
        # Log unexpected errors and notify the user
        print(f"Unexpected error: {error}")
        await send_error_embed("Unexpected error",
                               f'An unexpected error has occurred. Please try again later or contact `@jobcuenca`')
        await send_error_embed("Error inesperado",
                               f'Un error inesperado ha ocurrido. Por favor vuelva a intentarlo más tarde o contacte con @jobcuenca')

# Handle bot commands
@bot.command()
async def rae(ctx, *, message) -> None:
    await ctx.send(embed=get_rae_results(message))

@bot.command()
async def help(ctx) -> None:
    await ctx.send(embed=show_help())

# Print bot status
@bot.event
async def on_ready() -> None:
    print(f"Roboj is now live as {bot.user}!")

# Handle main entry point
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()