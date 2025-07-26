class Vacancy:
    """Класс для создания вакансий"""

    def __init__(self, name, url, descriptions, requirements, salary=None) -> None:
        self.name = name
        self.url = url
        self.salary = self.validate_salary(salary)
        self.descriptions = descriptions
        self.requirements = requirements

    def validate_salary(self, salary: dict) -> dict:
        """Валидирует данные о зарплате"""
        if salary is None:
            return {"from": 0, "to": 0, "currency": "не указана"}

        validated = {
            "from": salary.get("from", 0) or 0,
            "to": salary.get("to", 0) or 0,
            "currency": salary.get("currency", "не указана") or "не указана",
        }

        return validated

    def get_max_salary(self) -> int:
        """Возвращает максимальное значение зарплаты (из 'from' или 'to')"""
        return max(self.salary["from"], self.salary["to"])

    def salary_comparisons(self, other) -> str:
        """Сравнивает вакансии по максимальному значению зарплаты"""
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")

        self_max = self.get_max_salary()
        other_max = other.get_max_salary()

        if self_max > other_max:
            return f'Зарплата "{self.name}" ({self_max}) > "{other.name}" ({other_max})'
        elif self_max < other_max:
            return f'Зарплата "{other.name}" ({other_max}) > "{self.name}" ({self_max})'
        else:
            return f'Зарплаты "{self.name}" и "{other.name}" равны ({self_max})'
