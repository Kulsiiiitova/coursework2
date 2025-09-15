import json
import os

from JOB_VACANCY import VacancyStorage
from Vacancy import Vacancy


class JobVacancyData(VacancyStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_vacancy_to_file(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в файл"""
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        vacancy_dict = {
            "name": vacancy.name,
            "url": vacancy.url,
            "descriptions": vacancy.descriptions,
            "requirements": vacancy.requirements,
            "salary": vacancy.salary,
        }
        data.append(vacancy_dict)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def getting_data(self, param: dict) -> list[dict]:
        """Ищет вакансии по заданным параметрам"""
        filtered_vacancies = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                flag = True
                for key, value in param.items():
                    # Обрабатываем вложенные поля (например, salary.from)
                    if "." in key:
                        parts = key.split(".")
                        current = vacancy
                        try:
                            for part in parts[:-1]:
                                current = current[part]
                            if current[parts[-1]] != value:
                                flag = False
                                break
                        except (KeyError, TypeError):
                            flag = False
                            break
                    # Обычные поля
                    elif vacancy.get(key) != value:
                        flag = False
                        break
                if flag:
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def del_information(self, param: dict) -> None:
        """Удаляет вакансии по заданным параметрам"""
        filtered_vacancies = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
        for vacancy in vacancies:
            flag = True
            for key, value in param.items():
                if vacancy[key] == value:
                    flag = False
                    break
                if flag:
                    filtered_vacancies.append(vacancy)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(filtered_vacancies, f, ensure_ascii=False, indent=4)
