# -*- coding: utf-8 -*-

def split_list(items: list) -> list:

    length = len(items)

    if length == 0:
        return [[], []]
    elif length == 1:
        return [[items[0]], []]
    else:
        half = int(length / 2)
        if length % 2 == 0:
            return [items[:half], items[half:]]
        else:
            half = int(half) + 1
            return [items[:half], items[half:]]

