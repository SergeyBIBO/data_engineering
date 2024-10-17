from Utils.utils1 import Human, Company, Regiment
from datetime import datetime

persona00 = Human('Zokhan', datetime(2003,11,22))
persona01 = Human('Jackie', datetime(1999,12,12))
persona02 = Human('Jhurab', datetime(1989,7,15))
persona03 = Human('Scater', datetime(1990,6,3))
persona04 = Human('Hoosie', datetime(2002,5,7))
persona05 = Human('Spacie', datetime(2001,4,19))
persona06 = Human('Kassie', datetime(1993,10,27))
persona07 = Human('Jordan', datetime(1983,12,15))
persona08 = Human('Eithan', datetime(1988,11,14))

company00 = Company('#1 Alpha', [persona00, persona01, persona02])
company00.add_human([persona03, persona04, persona05])
company01 = Company('#2 Donetsk', [persona06, persona07, persona08])

regiment00 = Regiment([company00])
regiment00.add_company([company01])
regiment00.show_regiment()



