import requests

from parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> list[dict]:
        """Загружает вакансии по ключевому слову из API HeadHunter"""
        self.params["text"] = keyword
        self.params["page"] = 0
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json().get("items", [])
