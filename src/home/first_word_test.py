# -*- coding: utf-8 -*-

from src.home.first_word import first_word


def test_one_word():
    assert first_word('Hello world') == 'Hello'


def test_one_word():
    assert first_word(' a word') == 'a'


def test_word_with_aphostrophe():
    assert first_word(" It's finish") == "It's"
