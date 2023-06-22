if __name__ == '__main__':

    #  Александр Сергеевич Пушкин родился 26 мая 1799г
    real_year_born = 1799
    real_year_day  = 26
    year_born = None
    day_born = None

    true_year = True
    true_day = True
    while true_year:
        
        year_born = input("Введите год рождения А.С.Пушкина: ")

        if year_born.isdigit():
            if int(year_born) == real_year_born:
                true_year = False
                while true_day:
                    day_born = input("Введите день рождения А.С.Пушкина: ")
                    if day_born.isdigit():
                        if int(day_born) == real_year_day:
                            true_day = False
                            print("Верно")
                        else:
                            print("Неверный день рождения")
                    else:
                        print(f"Введенный день рождения {day_born} - не является числом")
            else:
                print("Неверный год рождения")
        else:
            print(f"Введенный год рождения {year_born} - не является числом")

