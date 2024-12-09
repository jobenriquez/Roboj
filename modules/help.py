import logging
import discord

def show_help() -> discord.Embed:
    help_english = ('### Available commands:\n'
                      '* `rae` - Look up definitions of a word from the Real Academia Española dictionary.\n'
                      '  * Example usage: `j! rae libro`.\n\n'
                      'Roboj is a Discord bot developed by `@jobcuenca`. For inquiries, suggestions, '
                      'and problem reports, you can contact him through the provided Discord account.')
    help_spanish = ('### Comandos disponibles:\n'
                    '* `rae` - Buscar definiciones de palabras del Diccionario de la Real Academia Española.\n'
                    '  * Ejemplo de uso: `j! rae libro`.\n\n'
                    'Roboj es un bot de discord desarrollado por `@jobcuenca`. Para consultas, sugerencias '
                    'e informes de problemas, pueda contactar con él a través de su cuenta de Discord.')

    embedded_help = discord.Embed(title="Roboj Help",
                                  description=help_english + '\n\n' + help_spanish,
                                  color=discord.Color.green())

    return embedded_help