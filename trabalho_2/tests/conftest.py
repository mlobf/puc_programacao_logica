"""Usando conftest"""

import pytest
import tests.sample_module as sm

@pytest.fixture()
def sample_numbers_unsorted() -> list[int]:
    return [-1, 3, 2, 1, 0]


@pytest.fixture(autouse=True)
def disable_api_data():
    get_api_data = lambda: "MODIFIED DATA"


def reverse_text(text: str) -> str:
    if isinstance(text, str):
        return text[::-1]
    else:
        raise TypeError


def get_api_data() -> str:
    return "ORIGINAL DATA"


def test_api_returns_data():
    actual = get_api_data()
    expected = "???"
    assert actual == expected



