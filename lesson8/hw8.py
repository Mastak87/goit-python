from datetime import datetime,timedelta


users = [{'Andrii': datetime(year=2021, month=8, day=9)}, {'Petro': datetime(year=2021, month=5, day=21)},
         {'Maksym': datetime(year=2021, month=7, day=20)}, {'Ivan': datetime(year=2021, month=5, day=21)},
         {'Bogdan': datetime(year=2021, month=5, day=15)}, {'Oleg':datetime(year=2021, month=5, day=18)}]


def congratulate(users):

    first_day = datetime.now() + timedelta(weeks=1) - timedelta(days=1)
    last_day = first_day + timedelta(weeks=1) - timedelta(days=1)
    week_first_day = timedelta(days=0)
    week_last_day = timedelta(days=7)

    week_birthdays = {}

    for i in users:

        for k, v in i.items():
            name = k
            birthday = v.strftime("%A")
            if last_day - v < week_last_day and last_day - v > week_first_day:
                week_birthdays[name] = birthday

    sort_week_birthdays = {}

    for names, day in week_birthdays.items():
        char = day
        if char not in sort_week_birthdays:
            sort_week_birthdays[char] = []
        sort_week_birthdays[char].append(names)

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sort_by_day = {}

    for day in week_days:
        if day in sort_week_birthdays:
            sort_by_day[day] = sort_week_birthdays[day]

    birthday_list = ''

    for k,v in sort_by_day.items():
        names = ', '.join(v)
        birthday_list += f'{k}: {names}\n'

    return birthday_list

if __name__ == '__main__':
    print(congratulate(users))