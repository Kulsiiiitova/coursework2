from classAPI import HH
from job_vacancy_data import JobVacancyData
from Vacancy import Vacancy


def main():
    """Главная функция"""
    hh_api = HH()
    storage = JobVacancyData("data/vacancies.json")
    search_query = input("Введите запрос для запроса вакансии из hh.ru: ")
    vacancies_data = hh_api.load_vacancies(search_query)
    vacancies = []
    for item in vacancies_data:
        try:
            description_items = []
            if item.get("experience", {}).get("name"):
                description_items.append(
                    f"Требуемый опыт: {item['experience']['name']}"
                )

            if item.get("professional_roles"):
                roles = ", ".join([role["name"] for role in item["professional_roles"]])
                description_items.append(f"Профессиональные роли: {roles}")

            if item.get("employment", {}).get("name"):
                description_items.append(f"Тип занятости: {item['employment']['name']}")
            full_description = ". ".join(description_items)
            vacancy = Vacancy(
                name=item["name"],
                url=item["alternate_url"],
                salary=item["salary"],
                descriptions=full_description,
                requirements=item["snippet"]["requirement"],
            )
            vacancies.append(vacancy)
            storage.add_vacancy_to_file(vacancy)
        except ValueError as e:
            print(f"Ошибка при обработке вакансии: {e}")
    count_vacancies = int(input("Введите количество топ вакансий по зарплате: "))
    sorted_vacancies = sorted(
        vacancies, key=lambda x: max(x.salary["from"], x.salary["to"]), reverse=True
    )[:count_vacancies]
    print("\nТоп вакансий по зарплате:")
    for i, vacancy in enumerate(sorted_vacancies, 1):
        salary_from = vacancy.salary["from"]
        salary_to = vacancy.salary["to"]
        currency = vacancy.salary.get("currency", "RUR")
        print(f"{i}. {vacancy.name}")
        print(f"Зарплата: {salary_from} - {salary_to} {currency}")
        print(f"Ссылка: {vacancy.url}\n")
    keywords = input("Введите ключевое слово: ")
    for vacancy in sorted_vacancies:
        if keywords in vacancy.requirements:
            print(f"{vacancy.name} - {vacancy.requirements}")
            print(f"{vacancy.url}\n")


if __name__ == "__main__":
    main()
