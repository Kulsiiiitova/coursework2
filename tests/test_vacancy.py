def test_vacancy_init(first_vacancy):
    assert first_vacancy.name == "Python Developer"
    assert first_vacancy.url == "https://example.com/python-dev"

    assert first_vacancy.descriptions == "Разработка на Python, Django, Flask"
    assert first_vacancy.requirements == "Опыт работы от 3 лет, знание SQL"
    assert first_vacancy.salary["from"] == 0
    assert first_vacancy.salary["to"] == 280000
    assert first_vacancy.salary["currency"] == "RUB"


def test_vacancy_zero_salary(second_vacancy):
    assert second_vacancy.salary["to"] == 0
    assert second_vacancy.salary["from"] == 0
    assert second_vacancy.salary["currency"] == "не указана"


def test_max_salary(first_vacancy):
    assert first_vacancy.get_max_salary() == 280000


def test_salary_comparisons(first_vacancy, second_vacancy):
    assert (
        first_vacancy.salary_comparisons(second_vacancy)
        == 'Зарплата "Python Developer" (280000) > "Python Developer" (0)'
    )
