from unittest.mock import Mock, patch

import pytest

from src.classAPI import HH
from src.parser import Parser


@pytest.fixture
def mock_api_response():
    return {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://example.com/vacancy1",
                "salary": {"from": 100000, "to": 150000, "currency": "RUB"},
                "snippet": {"requirement": "Опыт работы 3+ года"},
            }
        ]
    }


def test_hh_inherits_from_parser():
    """Тест что класс HH наследуется от Parser"""
    assert issubclass(HH, Parser)


@patch("requests.get")
def test_load_vacancies_success(mock_get, mock_api_response):
    """Тест успешной загрузки вакансий"""
    # Настраиваем mock
    mock_response = Mock()
    mock_response.json.return_value = mock_api_response
    mock_get.return_value = mock_response

    hh = HH()
    vacancies = hh.load_vacancies("Python")

    # Проверяем результаты
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[0]["salary"]["from"] == 100000

    # Проверяем параметры запроса
    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "Python", "page": 0, "per_page": 100},
    )


@patch("requests.get")
def test_load_vacancies_empty(mock_get):
    """Тест пустого ответа от API"""
    mock_get.return_value.json.return_value = {"items": []}

    hh = HH()
    vacancies = hh.load_vacancies("Несуществующий запрос")
    assert vacancies == []
