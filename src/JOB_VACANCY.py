from abc import ABC, abstractmethod


class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def getting_data(self):
        pass

    def del_information(self):
        pass
