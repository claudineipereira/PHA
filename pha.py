#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Bcolors:
    YELLOW = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


while True:
    try:
        name = input(f"Digite o nome do autor no formato {Bcolors.BOLD}\"Sobrenome, nome\"{Bcolors.ENDC}: ")

        if name == "Q":
            break

        first = name.split(",")[1].lstrip()
        last = name.split(",")[0]
        pha_url = requests.get(f"https://cuttersonline.com/app/generator/?q={name}&ref=pha")

        if pha_url.status_code == requests.codes.ok:
            soup = BeautifulSoup(pha_url.text, "lxml")
            pha_number = soup.h4.strong.text
            print(f"Código PHA para \"{first} {last}\": {Bcolors.YELLOW}{pha_number}{Bcolors.ENDC}\n")

    except IndexError:
        print(f"Por favor utilize o formato {Bcolors.BOLD}\"Sobrenome, nome\"{Bcolors.ENDC}.")

