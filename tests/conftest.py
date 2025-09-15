import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def first_vacancy():
    return Vacancy(
        name="Python Developer",
        url="https://example.com/python-dev",
        descriptions="Разработка на Python, Django, Flask",
        requirements="Опыт работы от 3 лет, знание SQL",
        salary={"from": 0, "to": 280000, "currency": "RUB"},
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        name="Python Developer",
        url="https://example.com/python-dev",
        descriptions="Разработка на Python, Django, Flask",
        requirements="Опыт работы от 3 лет, знание SQL",
        salary=None,
    )


@pytest.fixture
def third_vacancy():
    return Vacancy(
        name="Data Scientist",
        url="https://example.com/data-scientist",
        descriptions="Анализ данных",
        requirements="Знание Python",
        salary={"from": 0, "to": 100000, "currency": "RUB"},
    )
