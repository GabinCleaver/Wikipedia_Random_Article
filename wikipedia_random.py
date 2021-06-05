from bs4 import BeautifulSoup
import requests
from colorama import Fore, init

init()

try:
    res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    res.raise_for_status()

    wiki = BeautifulSoup(res.text, "html.parser")

    r = open("random_wiki.txt", "w+", encoding='utf-8')

    heading = wiki.find("h1").text

    r.write(heading + "\n")
    for i in wiki.select("p"):
        r.write(i.getText())

    r.close()

    print(Fore.GREN + "Fichier enregistré sous le nom de random_wiki.txt")
except:
    print(Fore.RED + "Erreur dans la création du fichier.")
