def calc():
    kalkulator = input("Wybierz działanie(+, -, *, /, %, **): ")

    if kalkulator == "+":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik dodawania:", int(x) + int(y))
    elif kalkulator == "-":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik odejmowania:", int(x) - int(y))
    elif kalkulator == "*":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik mnożenia:", int(x) * int(y))
    elif kalkulator == "/":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik dzielenia:", int(x) / int(y))
    elif kalkulator == "%":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik reszty z dzielenia:", int(x) % int(y))
    elif kalkulator == "**":
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik potęgowania:", int(x) ** int(y))
    elif kalkulator != "+" or "-" or "*" or "/" or "%" or "**":
        print("Błędne działanie, wybierz ponownie.")
        calc()

calc()
