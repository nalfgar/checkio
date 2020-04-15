# -*- coding: utf-8 -*-

from collections import Counter


def popular_words(text: str, words: list) -> dict:
    result = {}

    splited_text = Counter(text.lower().split())

    for i in words:
        result[i] = splited_text[i]

    return result
