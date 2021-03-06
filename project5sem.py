import requests
from bs4 import BeautifulSoup
!pip install pycbrf
from pycbrf.toolbox import ExchangeRates

x1 = input("Чтобы узнать текущий курс - нажмите 1 \nЧтобы узнать курс определенной даты - нажмите 2:\n")

if x1 == "1":
    url = 'https://finance.rambler.ru/currencies/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}


    def currency_usd_rub():
        page = requests.get(url, headers=headers)
        pars = BeautifulSoup(page.content, 'html.parser')
        tags = pars.findAll('div', {'class': 'finance-currency-table__cell finance-currency-table__cell--value'})
        return tags[29].text


    usd_rub = currency_usd_rub().replace(",", ".")
    usd_rub = float(usd_rub)


    def currency_euro_rub():
        page = requests.get(url, headers=headers)
        pars = BeautifulSoup(page.content, 'html.parser')
        tags = pars.findAll('div', {'class': 'finance-currency-table__cell finance-currency-table__cell--value'})
        return tags[11].text


    euro_rub = currency_euro_rub().replace(",", ".")
    euro_rub = float(euro_rub)


    def currency_gbp_rub():
        page = requests.get(url, headers=headers)
        pars = BeautifulSoup(page.content, 'html.parser')
        tags = pars.findAll('div', {'class': 'finance-currency-table__cell finance-currency-table__cell--value'})
        return tags[12].text


    gbp_rub = currency_gbp_rub().replace(",", ".")
    gbp_rub = float(gbp_rub)

    rub_euro = 1 / euro_rub
    rub_usd = 1 / usd_rub
    rub_gbp = 1 / gbp_rub
    euro_usd = euro_rub / usd_rub
    euro_gbp = euro_rub / gbp_rub
    usd_euro = usd_rub / euro_rub
    usd_gbp = usd_rub / gbp_rub
    gbp_usd = gbp_rub / usd_rub
    gbp_euro = gbp_rub / euro_rub

    ex = input("Выберите конвертируемую валюту(USD, EUR, RUB, GBP): ")
    ex2 = input("Выберите валюту, в которую хотите конвертировать(USD, EUR, RUB, GBP): ")

    if ex == "USD":
        if ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * usd_rub
            print(inf, "USD =", result, "RUB по нынешнему курсу")
        elif ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * usd_euro
            print(inf, "USD =", result, "EUR по нынешнему курсу")
        elif ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * usd_gbp
            print(inf, "USD =", result, "GBP по нынешнему курсу")
        else:
            print("Выбранной валюты нет в программе.")

    elif ex == "EUR":
        if ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * euro_rub
            print(inf, "EUR =", result, "RUB по нынешнему курсу")
        elif ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * euro_usd
            print(inf, "EUR =", result, "USD по нынешнему курсу")
        elif ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * euro_gbp
            print(inf, "EUR =", result, "GBP по нынешнему курсу")
        else:
            print("Выбранной валюты нет в программе.")

    elif ex == "RUB":
        if ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * rub_usd
            print(inf, "RUB =", result, "USD по нынешнему курсу")
        elif ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * rub_euro
            print(inf, "RUB =", result, "EUR по нынешнему курсу")
        elif ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * rub_gbp
            print(inf, "RUB =", result, "GBP по нынешнему курсу")
        else:
            print("Выбранной валюты нет в программе.")
    elif ex == "GBP":
        if ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * gbp_usd
            print(inf, "GBP =", result, "RUB по нынешнему курсу")
        elif ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * gbp_euro
            print(inf, "GBP =", result, "EUR по нынешнему курсу")
        elif ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * gbp_rub
            print(inf, "GBP =", result, "RUB по нынешнему курсу")
        else:
            print("Выбранной валюты нет в программе.")
    else:
        print("Выбранной валюты нет в программе.")


else:
    choice = input("Напишите нужную дату(в формат гггг-мм-дд)")
    rates = ExchangeRates(choice)
    old_euro_rub = float(rates['EUR'][4])
    old_usd_rub = float(rates['USD'][4])
    old_gbp_rub = float(rates['GBP'][4])
    old_rub_euro = 1 / old_euro_rub
    old_rub_usd = 1 / old_usd_rub
    old_rub_gbp = 1 / old_gbp_rub
    old_euro_usd = old_euro_rub / old_usd_rub
    old_euro_gbp = old_euro_rub / old_gbp_rub
    old_usd_euro = old_usd_rub / old_euro_rub
    old_usd_gbp = old_usd_rub / old_gbp_rub
    old_gbp_usd = old_gbp_rub / old_usd_rub
    old_gbp_euro = old_gbp_rub / old_euro_rub

    old_ex = input("Выберите конвертируемую валюту(USD, EUR, RUB, GBP): ")
    old_ex2 = input("Выберите валюту, в которую хотите конвертировать(USD, EUR, RUB, GBP): ")

    if old_ex == "USD":
        if old_ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * old_usd_rub
            print(inf, "USD =", result, "RUB по курсу на", choice)
        elif old_ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * old_usd_euro
            print(inf, "USD =", result, "EUR по курсу на", choice)
        elif old_ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * old_usd_gbp
            print(inf, "USD =", result, "GBP по курсу на", choice)
        else:
            print("Выбранной валюты нет в программе.")

    elif old_ex == "EUR":
        if old_ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * old_euro_rub
            print(inf, "EUR =", result, "RUB по курсу на", choice)
        elif old_ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * old_euro_usd
            print(inf, "EUR =", result, "USD по курсу на", choice)
        elif old_ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * old_euro_gbp
            print(inf, "EUR =", result, "GBP по курсу на", choice)
        else:
            print("Выбранной валюты нет в программе.")

    elif old_ex == "RUB":
        if old_ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * old_rub_usd
            print(inf, "RUB =", result, "USD по курсу на", choice)
        elif old_ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * old_rub_euro
            print(inf, "RUB =", result, "EUR по курсу на", choice)
        elif old_ex2 == "GBP":
            inf = float(input("Введите число: "))
            result = inf * old_rub_gbp
            print(inf, "RUB =", result, "GBP по курсу на", choice)
        else:
            print("Выбранной валюты нет в программе.")
            
    elif old_ex == "GBP":
        if old_ex2 == "USD":
            inf = float(input("Введите число: "))
            result = inf * old_gbp_usd
            print(inf, "GBP =", result, "RUB по курсу на", choice)
        elif old_ex2 == "EUR":
            inf = float(input("Введите число: "))
            result = inf * old_gbp_euro
            print(inf, "GBP =", result, "EUR по курсу на", choice)
        elif old_ex2 == "RUB":
            inf = float(input("Введите число: "))
            result = inf * old_gbp_rub
            print(inf, "GBP =", result, "RUB по курсу на", choice)
        else:
            print("Выбранной валюты нет в программе.")
    else:
        print("Выбранной валюты нет в программе.")
