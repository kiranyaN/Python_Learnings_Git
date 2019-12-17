from datetime import datetime
def ObtainDate():
    entry = input("Type Date dd/mm/year: ")
    d = datetime.strptime(input, "%y-%m-%d")
    return
ObtainDate()
