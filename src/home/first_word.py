# -*- coding: utf-8 -*-

import re

def first_word(text: str) -> str:

    pattern = re.compile(r"[a-zA-Z']+")

    return re.findall(pattern, text)[0]
