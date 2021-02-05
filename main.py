from datetime import datetime
from application.db import people as people1

def parametrized_decor(path):
    def decor(foo):
        def new_foo(*args, **kwargs):
            result = foo()
            now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
            with open("logs.txt", "w") as f:
                f.write(f"{now} - {foo.__name__} - args: {args, kwargs} res: {result} \n")
            return result
        return new_foo
    return decor

@parametrized_decor("logs.txt")
def calc_salary():
    return print("prints smth")

if __name__ == '__main__':
    date = datetime.today()
    print(date)
    calc_salary(people1.get_employees())