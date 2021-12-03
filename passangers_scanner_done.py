restricted = ["нож", "бензин", "граната", "пистолет"]

passengers = [
    {
        "место": 0,
        "имя": "Питонов Василий Аспидович",
        "ручная кладь": ["ноутбук", "наушники"]
    },
    {
        "место": 1,
        "имя": "Блинохватов Прохор Аскольдович",
        "ручная кладь": ["книга", "четки", "беруши"]
    },
    {
        "место": 2,
        "имя": "Бабахин Капитон Кондратьевич",
        "ручная кладь": ["семечки", "граната", "кепка"]
    },
    {
        "место": 3,
        "имя": "Бескровная Таисия Ипатовна",
        "ручная кладь": ["журнал", "букет", "горсть земли"]
    },
    {
        "место": 4,
        "имя": "Аскетов Демьян Захарьевич",
        "ручная кладь": []
    }
]

print("Пассажиров на проверке:", len(passengers), "\n")

for passenger in passengers:
    for item in passenger["ручная кладь"]:
        if item in restricted:
            print("В ручной клади пассажира на месте", passenger["место"], "обнаружен запрещенный предмет", item)
            print("Пассажир", passenger["имя"], "не допущен к вылету")
            passengers.pop(passengers.index(passenger))

print("\nДопущено к вылету пассажиров:", len(passengers), "\n")

for passenger in passengers:
    for k, v in passenger.items():
        print(k, ":", v)
    print("")