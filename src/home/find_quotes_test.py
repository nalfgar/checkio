# -*- coding: utf-8 -*-


from src.home.find_quotes import find_quotes


def test_word_without_quotes():
    assert find_quotes('Hi') == []
