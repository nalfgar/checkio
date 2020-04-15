# -*- coding: utf-8 -*-


from src.home.find_quotes import find_quotes


def test_word_without_quotes():
    assert find_quotes('Hi') == []


def test_word_with_quotes():
    assert find_quotes('"Hi"') == ['Hi']


def test_three_word_with_quotes():
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
                       'of the printing and typesetting '
                       'industry. Lorem Ipsum has been the '
                       '"industry\'s standard dummy text '
                       'ever since the 1500s", when an '
                       'unknown printer took a galley of '
                       'type and scrambled it to make a type '
                       'specimen book. It has survived not '
                       'only five centuries, but also the '
                       'leap into electronic typesetting, '
                       'remaining essentially unchanged. "It '
                       'was popularised in the 1960s" with '
                       'the release of Letraset sheets '
                       'containing Lorem Ipsum passages, and '
                       'more recently with desktop '
                       'publishing software like Aldus '
                       'PageMaker including versions of '
                       'Lorem Ipsum.') == ['Lorem Ipsum',
                                           "industry's standard dummy text ever "
                                           'since the 1500s',
                                           'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']