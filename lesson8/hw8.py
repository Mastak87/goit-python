from datetime import datetime,timedelta



users = [{'Andrii': datetime(year=2021, month=8, day=9)}, {'Petro': datetime(year=2021, month=5, day=21)},
         {'Maksym': datetime(year=2021, month=7, day=20)}, {'Ivan': datetime(year=2021, month=5, day=21)},
         {'Bogdan': datetime(year=2021, month=5, day=15)}, {'Oleg':datetime(year=2021, month=5, day=18)}]

next_week = datetime.now() + timedelta(weeks=1) - timedelta(days=1)
next_week_2 = next_week + timedelta(weeks=1) - timedelta(days=1)
week = timedelta(days=7)
week_zero = timedelta(days=0)

def congratulate(users):
    week_birthdays = ''
    for i in users:

        for k, v in i.items():
            name = k
            birthday = v.strftime("%A")
            if next_week_2 - v < week and next_week_2 - v > week_zero:
                week_birthdays += f'{birthday}: {name}\n'

    return week_birthdays

if __name__ == '__main__':
    print(congratulate(users))