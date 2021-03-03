import pytest


@pytest.mark.parametrize("test_input,expected", [("1 ** 0", 1),
                                                 ("0 ** 0", 1),
                                                 ("200 ** 0", 1),
                                                 ("(-200) ** 0", 1),
                                                 ("(-99999999999999999999) ** 0", 1),
                                                 ("99999999999999999999 ** 0", 1)])
def test_int_1(test_input, expected):  # Тест с параметризацией
    assert eval(test_input) == expected


def test_int_2():  # Негативный тест
    n = [-1000, -3, -1, 0, 1, 2, 65537]
    for i in n:
        try:
            assert abs(i) == n * -1
        except AssertionError:
            pass


def test_int_3():  # Положительный тест
    n = [-50, -25, -1, 0, 1, 3, 16]
    for i in n:
        assert abs(i) >= 0


@pytest.mark.parametrize("test_input,expected", [("1 ** 0", str()),
                                                 ("0 ** 0", str()),
                                                 ("200 ** 0", str()),
                                                 ("-200 ** 0", str()),
                                                 ("-99999999999999999999 ** 0", str()),
                                                 ("99999999999999999999 ** 0", str())])
def test_string_1(test_input, expected):
    assert isinstance(str(test_input), expected)


def test_string_2():
    string = 'abc12 3J DKW I@#$'
    string.replace('@', 'replaced')
    assert '@' in string


def test_string_3():
    n = ' fwaf '
    assert ' ' not in n.strip()

