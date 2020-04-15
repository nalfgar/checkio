# -*- coding: utf-8 -*-
import pytest

from src.home.sum_numbers import sum_numbers


def test_empty_inscription():
    assert sum_numbers('') == 0


def test_only_letters_in_inscription():
    assert sum_numbers('Hi') == 0


def test_one_digit():
    assert sum_numbers('12') == 12


def test_two_digit():
    assert sum_numbers('12 12') == 24


def test_two_digit_witch_numerator():
    assert sum_numbers('12 12 1st') == 24
