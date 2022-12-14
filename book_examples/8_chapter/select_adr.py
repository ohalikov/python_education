ADR_MAP = {
    "1": {
        "exname": "Отдел предоставления услуг № 1 по Петрозаводскому городскому округу",
        "mfc_id": 8546,
        "id": 1,
        "name": "Филиал в городе Петрозаводск на набережной Г+юллинга, дом 11",
    },
    "2": {
        "exname": "Отдел предоставления услуг № 2 по Петрозаводскому городскому округу",
        "mfc_id": 3149,
        "id": 2,
        "name": "Филиал в городе Петрозаводск, Первомайский Проспект, дом 33",
    },
    "3": {
        "exname": "ЦОУ для бизнеса ОПУ № 2",
        "mfc_id": 6725,
        "id": 3,
        "name": "Филиал в городе Петрозаводск по улице Андропова, дом 15 ",
    },
    "4": {
        "exname": "Отдел предоставления услуг № 4 по Кондопожскому муниципальному району",
        "mfc_id": 6749,
        "id": 4,
        "name": "Филиал в городе Кондопога, проспект Калинина, дом 13",
    },
    "5": {
        "exname": "Отдел предоставления услуг № 5 по Пряжинскому национальному муниципальному району",
        "mfc_id": 3696,
        "id": 5,
        "name": "Филиал в поселке городского типа Пряжа по улице Петрозаводская, дом 16",
    },
    "6": {
        "exname": "Отдел предоставления услуг № 6 по Олонецкому национальному муниципальному району",
        "mfc_id": 564,
        "id": 6,
        "name": "Филиал в городе Олонец по улице Полевая, дом 39",
    },
    "7": {
        "exname": "Отдел предоставления услуг № 7 по Медвежьегорскому муниципальному району",
        "mfc_id": 3782,
        "id": 7,
        "name": "Филиал в городе Медвежьегорск по улице Советская, дом 18",
    },
    "8": {
        "exname": "Отдел предоставления услуг № 8 по Пудожскому муниципальному району",
        "mfc_id": 689,
        "id": 8,
        "name": "Филиал в городе Пудож по улице Карла Маркса, дом 45",
    },
    "9": {
        "exname": "Отдел предоставления услуг № 9 по Сегежскому муниципальному району",
        "mfc_id": 6458,
        "id": 9,
        "name": "Филиал в городе Сегежа по адресу: проезд Монтажников, дом 7",
    },
    "10": {
        "exname": "Отдел предоставления услуг № 10 по Беломорскому муниципальному району",
        "mfc_id": 1212,
        "id": 10,
        "name": "Филиал в городе Беломорск по улице Первомайская, дом 8",
    },
    "11": {
        "exname": "Отдел предоставления услуг № 11 по Кемскому муниципальному району",
        "mfc_id": 3434,
        "id": 11,
        "name": "Филиал в городе Кемь по улице Каменева, дом 12",
    },
    "12": {
        "exname": "Отдел предоставления услуг № 12 по Лоухскому муниципальному району",
        "mfc_id": 646,
        "id": 12,
        "name": "Филиал в поселке городского типа Лоухи по улице Жаровина, дом 30",
    },
    "13": {
        "exname": "Отдел предоставления услуг № 13 по Калевальскому национальному району",
        "mfc_id": 828,
        "id": 13,
        "name": "Филиал в поселке городского типа Калевала по улице Калевалы, дом 14",
    },
    "14": {
        "exname": "Отдел предоставления услуг № 14 по Муезерскому муниципальному району",
        "mfc_id": 321,
        "id": 14,
        "name": "Филиал в поселке городского типа Муезерский по улице Октябрьская, дом 35",
    },
    "15": {
        "exname": "Отдел предоставления услуг № 15 по Костомукшскому городскому округу",
        "mfc_id": 456,
        "id": 15,
        "name": "Филиал в городе Костомукша по улице Надежды, дом 5",
    },
    "16": {
        "exname": "Отдел предоставления услуг № 16 по Суоярвскому муниципальному району",
        "mfc_id": 789,
        "id": 16,
        "name": "Филиал в городе Суоярви по улице Кайманова, дом 13",
    },
    "30": {
        "exname": "Отдел предоставления услуг № 3 по Петрозаводскому городскому округу",
        "mfc_id": 396,
        "id": 30,
        "name": "Филиал в городе Петрозаводск по адресу: Лососинское шоссе, дом 26",
    },
    "17": {
        "exname": "Отдел предоставления услуг № 17 по Питкярантскому муниципальному району",
        "mfc_id": 258,
        "id": 17,
        "name": "Филиал в городе Питкяранта по улице Горького дом 49, корпус г",
    },
    "18": {
        "exname": "Отдел предоставления услуг № 18 по Сортавальскому муниципальному району",
        "mfc_id": 148,
        "id": 18,
        "name": "Филиал в городе Сортавала по улице Комсомольская, дом 10, строение 7",
    },
    "19": {
        "exname": "Отдел предоставления услуг № 19 по  Лахденпохскому муниципальному району",
        "mfc_id": 147,
        "id": 19,
        "name": "Филиал в городе Лахденпохья по улице Бусалова, дом 3",
    },
}


def get_object_from_only_adr_map(filial_name):
    key_ids = ADR_MAP.keys()
    adr_object = [
        ADR_MAP[key]
        for key in key_ids
        if ADR_MAP[key]['exname'] == filial_name
    ]

    return adr_object[0] if len(adr_object) == 1 else None


exname = 'Отдел предоставления услуг № 18 по Сортавальскому муниципальному району'
adr_obj = get_object_from_only_adr_map(exname)
print(adr_obj)
