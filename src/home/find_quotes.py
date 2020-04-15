# -*- coding: utf-8 -*-

import re

def find_quotes(text: str) -> list:
    print(text)
    pattern = re.compile(r'""|"(\w+)"')

    return re.findall(pattern, text)




