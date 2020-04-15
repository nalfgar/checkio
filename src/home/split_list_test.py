# -*- coding: utf-8 -*-
import pytest

from src.home.split_list import split_list


def test_empty_list():
    assert split_list([]) == [[], []]


def test_one_element_list():
    assert split_list([1]) == [[1], []]


def test_two_element_list():
    assert split_list([1, 2]) == [[1], [2]]


def test_three_element_list():
    assert split_list([1, 2, 3]) == [[1, 2], [3]]


def test_four_list():
    assert split_list([1, 2, 3, 4]) == [[1, 2], [3, 4]]

def test_five_list():
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]


def test_six_list():
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
