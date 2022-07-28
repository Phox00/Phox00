import random

list_top = {"Акали", "Акшан", "Вай", "Вейн", "Вуконг", "Галио", "Гарен", "Грагас", "Грейвз", "Дариус", "Джакс",
            "Джарван", "Джейс", "Диана", "Доктор Мундо", "Ирелия", "Камилла", "Кейл", "Кеннен", "Корки", "Ксин Жао",
            "Ли Син", "Лулу", "Люциан", "Мальфит", "Насус", "Наутилус", "Нуну", "Олаф", "Пайк", "Пантеон",
            "Ренгар", "Ренектон", "Ривен", "Рэйкан", "Сетт", "Синджед", "Тимо", "Триндамир", "Тристана",
            "Фиора", "Шен", "Шивана", "Эзреал", "Экко", "Энни", "Ясуо"}

list_jungle = {"Амуму", "Вай", "Вейн", "Вуконг", "Грагас", "Грейвс", "Дариус", "Джакс", "Джарван", "Джейс",
               "Диана", "Доктор Мундо", "Ирелия", "Казикс", "Камилла", "Кейл", "Ксин Жао", "Ли Син", "Мастер Йи",
               "Моргана", "Насус", "Наутилус", "Нуну", "Олаф", "Пайк", "Пантеон", "Раммус", "Ренгар", "Рекектон",
               "Ривен", "Сетт", "Синджед" "Твистед Фейт", "Тимо", "Триндамир", "Физз", "Фиора", "Шен", "Шивана",
               "Эвелин", "Экко", "Ясуо"}

list_mid = {"Акали", "Акшан", "Ари", "Аурелион Сол", "Брэнд", "Варус", "Вейгар", "Галио", "Гарен", "Грагас",
            "Джейс", "Джин", "Диана", "Зед", "Зиггс", "Ирелия", "Карма", "Катарина", "Кейл", "Кеннен",
            "Корки", "Люкс", "Люциан", "Мальфит", "Моргана", "Орианна", "Пайк", "Пантеон", "Ривен", "Рэйкан",
            "Серафина", "Синджед", "Твистед Фейт", "Тимо", "Физз", "Эзреал", "Экко", "Энни", "Эш", "Ясуо"}

list_adc = {"Варус", "Вейн", "Джин", "Джинкс", "Дрейвен", "Зиггс", "Кайса", "Карма", "Кейтлин", "Корки",
            "Люкс", "Люциан", "Мисс Фортуна", "Орианна", "Сенна", "Твистед Фейт", "Тристана", "Шая", "Эзреал", "Эш"}

list_sup = {"Алистар", "Блицкранк", "Браум", "Галио", "Грагас", "Жанна", "Карма", "Леона", "Лулу", "Люкс",
            "Мальфит", "Моргана", "Нами", "Наутилус", "Пайк", "Пантеон", "Рэйкан", "Сенна", "Серафина", "Сетт",
            "Синджед", "Сона", "Сорака", "Твистед Фейт", "Треш", "Шен", "Энни", "Юми"}


phox_pull = {'Акали', 'Акшан', 'Амуму', 'Ари', 'Блицкранк', 'Брэнд', 'Вай', 'Варус', 'Вейн', 'Галио',
             'Гарен', 'Грагас', 'Грейвз', 'Дариус', 'Джакс', 'Джин', 'Джинкс', 'Дрейвен', 'Жанна',
             'Зиггс', 'Ирелия', 'Казикс', 'Кайса', 'Камилла', 'Катарина', 'Кейтлин', 'Кеннен', 'Ксин Жао',
             'Ли Син', 'Лулу', 'Люкс', 'Люциан', 'Мальфит', 'Мастер Йи', 'Мисс Фортуна', 'Моргана', 'Насус',
             'Олаф', 'Орианна', 'Пайк', 'Пантеон', 'Ривен', 'Рэйкан', 'Сенна', 'Серафина', 'Сетт', 'Твистед Фейт',
             'Триндамир', 'Физз', 'Фиора', 'Шая', 'Эвелинн', 'Экко', 'Энни', 'Эзреал', 'Эш', 'Ясуо'}
erseia_pull = {'Акали', 'Акшан', 'Алистар', 'Ари', 'Блицкранк', 'Брэнд', 'Вай', 'Вейгар', 'Галио', 'Гарен',
               'Джакс', 'Джинкс', 'Диана', 'Жанна', 'Зиггс', 'Ирелия', 'Кайса', 'Карма', 'Катарина', 'Кейл',
               'Кеннен', 'Леона', 'Лулу', 'Люкс', 'Мальфит', 'Мастер Йи', 'Мисс Фортуна', 'Моргана', 'Нами',
               'Насус', 'Наутилус', 'Орианна', 'Пайк', 'Пантеон', 'Ренгар', 'Ренектон', 'Ривен', 'Рэйкан',
               'Сенна', 'Серафина', 'Сона', 'Сорака', 'Тимо', 'Триндамир', 'Физз', 'Фиора', 'Шая', 'Шивана',
               'Экко', 'Энни', 'Эш', 'Юми', 'Ясуо'}
elzark_pull = {"Алистар", "Ари", "Блицкранк", "Браум", "Вай", "Вуконг", "Гарен", "Дариус", "Джинкс",
               "Доктор Мундо", "Жанна", "Ирелия", "Катарина", "Леона", "Лулу", "Люкс", "Мальфит", "Мастер Йи",
               "Насус", "Нуну", "Пантеон", "Ривен", "Рэйкан", "Сенна", "Сетт", "Сона", "Сорака", "Твистед Фейт",
               "Треш", "Триндамир", "Физз", "Фиора", "Шая", "Шен", "Шивана", "Эвелинн", "Эзреал", "Энни",
               "Эш", "Юми", "Ясуо"}

while True:
    players = input("Who is playing?  (phox/elzark/erseia)  ").lower()
    while True:
        if "phox" in players:
            phox_top = random.sample(list(phox_pull.intersection(list_top)), k=2)
            phox_jungle = random.sample(list(phox_pull.intersection(list_jungle)), k=2)
            phox_mid = random.sample(list(phox_pull.intersection(list_mid)), k=2)
            phox_adc = random.sample(list(phox_pull.intersection(list_adc)), k=2)
            phox_sup = random.sample(list(phox_pull.intersection(list_sup)), k=2)

            print(f"""\n--------------------------------
        \tPhox
            
    Top:      {phox_top[0]}, {phox_top[1]}
    Jungle:   {phox_jungle[0]}, {phox_jungle[1]}
    Mid:      {phox_mid[0]}, {phox_mid[1]}
    Adc:      {phox_adc[0]}, {phox_adc[1]}
    Sup:      {phox_sup[0]}, {phox_sup[1]}
--------------------------------""")

        if "elzark" in players:
            elzark_top = random.sample(list(elzark_pull.intersection(list_top)), k=2)
            elzark_jungle = random.sample(list(elzark_pull.intersection(list_jungle)), k=2)
            elzark_mid = random.sample(list(elzark_pull.intersection(list_mid)), k=2)
            elzark_adc = random.sample(list(elzark_pull.intersection(list_adc)), k=2)
            elzark_sup = random.sample(list(elzark_pull.intersection(list_sup)), k=2)

            print(f"""\n--------------------------------
        \tElzark
    
    Top:      {elzark_top[0]}, {elzark_top[1]}
    Jungle:   {elzark_jungle[0]}, {elzark_jungle[1]}
    Mid:      {elzark_mid[0]}, {elzark_mid[1]}
    Adc:      {elzark_adc[0]}, {elzark_adc[1]}
    Sup:      {elzark_sup[0]}, {elzark_sup[1]}
--------------------------------""")

        if "erseia" in players:
            erseia_top = random.sample(list(erseia_pull.intersection(list_top)), k=2)
            erseia_jungle = random.sample(list(erseia_pull.intersection(list_jungle)), k=2)
            erseia_mid = random.sample(list(erseia_pull.intersection(list_mid)), k=2)
            erseia_adc = random.sample(list(erseia_pull.intersection(list_adc)), k=2)
            erseia_sup = random.sample(list(erseia_pull.intersection(list_sup)), k=2)

            print(f"""\n--------------------------------
        \tErseia
    
    Top:      {erseia_top[0]}, {erseia_top[1]}
    Jungle:   {erseia_jungle[0]}, {erseia_jungle[1]}
    Mid:      {erseia_mid[0]}, {erseia_mid[1]}
    Adc:      {erseia_adc[0]}, {erseia_adc[1]}
    Sup:      {erseia_sup[0]}, {erseia_sup[1]}
--------------------------------""")

        if input() == "exit":
            break
