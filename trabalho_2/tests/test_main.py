import pytest


@pytest.fixture()
def sample_numbers_unsorted() -> list[int]:
    return [-1, 3, 2, 1, 0]


def add_two_numbers(a: float, b: float) -> float:
    for num in [a, b]:
        if not isinstance(num, float | int):
            return 0
    return a + b


def sort_numbers(numbers: list[int]) -> list[int]:
    numbers.sort()
    return numbers


def reverse_numbers(numbers: list[int]) -> list[int]:
    numbers.reverse()
    return numbers


def test_sort_numbers(sample_numbers_unsorted):
    actual = sort_numbers(sample_numbers_unsorted)
    expected = [-1, 0, 1, 2, 3]
    assert actual == expected


def test_reverse_numbers(sample_numbers_unsorted):
    actual = reverse_numbers(sample_numbers_unsorted)
    expected = [0, 1, 2, 3, -1]
    print('actual -> ',actual)
    print('expected -> ',expected)
    assert actual == expected


class TestGroup:
    def test_one_plus_one_is_two(self):
        a, b = 1, 1
        actual = add_two_numbers(a, b)
        expected = 2
        assert actual == expected

    def test_one_plus_letter_returns_zero(self):
        a, b = 1, "a"
        actual = add_two_numbers(a, b)
        expected = 0
        assert actual == expected
