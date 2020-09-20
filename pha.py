#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

name = input("Sobrenome, nome: ")
pha_url = requests.get(f"https://cuttersonline.com/app/generator/?q={name}&ref=pha")


def phaResult():
    soup = BeautifulSoup(pha_url.text, "lxml")
    pha_number = soup.h4.strong.text
    print(f"\nCódigo PHA para \"{name}\": {pha_number}")


def pha():
    if pha_url.status_code == requests.codes.ok:
        phaResult()


if __name__ == "__main__":
    pha()
