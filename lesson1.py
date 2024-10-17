class Human:
    def __init__(self, name = 'DefaultArmyPerson', age = 0):
        self.name = name
        self.age = age
        self.__branch = 'Artillery'

    def get_info(self):
        return self.name + ': ' + str(self.age) + ' | ' + self.__branch

persona00 = Human('Zokhan', 24)
persona01 = Human('Jackie', 30)
persona02 = Human('Jhurab', 26)
persona03 = Human('Scater', 34)
persona04 = Human('Hoosie', 19)
persona05 = Human('Spacie', 29)
persona06 = Human('Kassie', 18)
persona07 = Human('Jordan', 22)
persona08 = Human('Eithan', 21)

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
            print(one_human.get_info())

company00 = Company('#1 Alpha', [persona00, persona01, persona02])
company01 = Company('#2 Bravo', [persona03, persona04, persona05])
company02 = Company('#3 Charlie', [persona06, persona07, persona08])

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

regiment00 = Regiment([company00, company01, company02])
regiment00.show_regiment()

