from datetime import datetime
from dateutil.relativedelta import relativedelta

class Human:

    def __init__(self, name = 'DefaultArmyPerson', birthday = datetime(2002,11,22)):
        self.name = name
        self.birthday = birthday
        self.__branch = 'Artillery'

    def get_age(self):
          current_date = datetime.now()
          age = relativedelta(current_date, self.birthday)
          return f"{age.years} лет"

    def get_info(self):
        return f"Имя: {self.name} | Дата рождения: {self.birthday.strftime('%Y-%m-%d')} | "

class Company:

    def __init__(self, text, humans: list):
        self.text = text
        self.humans = humans

    def add_human(self, humans: list):
        self.humans += humans

    def del_human(self, humans: list):
        for one_human in humans:
            if one_human in humans:
                self.humans.remove(one_human)

    def show_company(self):
        print('======= ' + self.text + ' ======')
        for one_human in self.humans:
            print(one_human.get_info() + one_human.get_age())

class Regiment:

    def __init__(self, companies: list):
        self.companies = companies

    def show_regiment(self):
        for one_company in self.companies:
            one_company.show_company()

    def add_company(self, companies: list):
        self.companies += companies

    def del_company(self, companies: list):
        for one_company in companies:
            if one_company in companies:
                self.companies.remove(one_company)