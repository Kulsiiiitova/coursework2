import json

import pytest

from src.job_vacancy_data import JobVacancyData


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_vacancies.json"


def test_add_vacancy_to_file(temp_file, first_vacancy):
    """Тест добавления вакансии в файл"""
    storage = JobVacancyData(temp_file)
    storage.add_vacancy_to_file(first_vacancy)

    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["name"] == "Python Developer"
        assert data[0]["salary"]["to"] == 280000


def test_add_multiple_vacancies(temp_file, first_vacancy, third_vacancy):
    """Тест добавления нескольких вакансий"""
    storage = JobVacancyData(temp_file)
    storage.add_vacancy_to_file(first_vacancy)
    storage.add_vacancy_to_file(third_vacancy)

    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["name"] == "Python Developer"
        assert data[1]["name"] == "Data Scientist"


def test_getting_data_by_param(temp_file, first_vacancy, third_vacancy):
    """Тест фильтрации вакансий по параметрам"""
    storage = JobVacancyData(temp_file)
    storage.add_vacancy_to_file(first_vacancy)
    storage.add_vacancy_to_file(third_vacancy)

    # Фильтр по имени
    result = storage.getting_data({"name": "Python Developer"})
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"

    # Фильтр по зарплате (используем вложенный доступ)
    result = storage.getting_data({"salary.to": 100000})
    assert len(result) == 1
    assert result[0]["name"] == "Data Scientist"


def test_del_information(temp_file, first_vacancy, third_vacancy):
    """Тест удаления вакансий по параметрам"""
    storage = JobVacancyData(temp_file)
    storage.add_vacancy_to_file(first_vacancy)
    storage.add_vacancy_to_file(third_vacancy)

    # Удаляем по имени
    storage.del_information({"name": "Python Developer"})

    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["name"] == "Data Scientist"
