import datetime

def year_of_birth():
    age = input("How old are you? ")
    return datetime.datetime.now().year - int(age)

if __name__ == '__main__':
    print(year_of_birth())
