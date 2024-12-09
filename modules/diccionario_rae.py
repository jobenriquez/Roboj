import logging
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import discord
import lxml

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def get_rae_results(input) -> discord.Embed:
    word = urllib.parse.quote(input)
    try:
        url = f"https://dle.rae.es/{word}/"

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, "lxml")
        article = soup.find("article")
        if not article:
            embedded_error = discord.Embed(title="Palabra no encontrada",
                                           description=f'La palabra `{input}` no existe en el diccionario. Por favor verifique que la palabra esté escrita correctamente.',
                                           color=0xFF5733)

            return embedded_error

        title = article.find("header", class_="f").text
        definitions = ""
        copyright = "© Real Academia Española, 2024."

        for definition in article.find_all("p", {"class": ["j", "j1", "j2", "j3", "j4", "j5", "j6", "l2"]}):
            if len(definitions + definition.text) < 2048:
                definitions += definition.text + "\n"

        embedded_result = discord.Embed(title=title, url=url,
                              description=f'{definitions}\n{copyright}',
                              color=discord.Color.blue())

        return embedded_result

    except Exception as e:
        logging.error(f"Error while processing message: {e}")

        embedded_error = discord.Embed(title="Error inesperado",
                                       description=f'Ha sido un error al procesar la palabra `{input}`. Inténtelo de nuevo más tarde o contacte con @jobcuenca.',
                                       color=0xFF5733)

        return embedded_error