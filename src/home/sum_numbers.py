# -*- coding: utf-8 -*-


def sum_numbers(text: str) -> int:
    total = 0
    if len(text) == 0:
        return total
    else:
        words = text.split()
        for word in words:
            if word.isdigit():
                total += int(word)
    return total
