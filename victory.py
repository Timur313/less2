if __name__ == '__main__':
    famous_people = [
        {"name": "Блок Александр Александрович", "year_born": 1880},
        {"name": "Высоцкий Владимир Семёнович", "year_born": 1938},
        {"name": "Грибоедов Александр Сергеевич", "year_born": 1795},
        {"name": "Маяковский Владимир Владимирович", "year_born": 1893},
        {"name": "Толстой Лев Николаевич", "year_born": 1828}
        ]

    restart = True
    while restart:
        print("Старт викторины!")
        print("Нужно угадать года рождения известных людей")
        true_res = 0
        for fam_peop in famous_people:
            fam_name = fam_peop["name"]
            real_year_born = fam_peop["year_born"]
            year_born = input(f"Введите год рождения {fam_name}: ")

            if year_born.isdigit():
                if int(year_born) == real_year_born:
                    true_res += 1
            else:
                print(f"{year_born} - не является числом. Ответ не засчитан!")
        print("Викторина завершена!")
        print("Статистика ответов:")
        print(f"Верно - {true_res} ({round(true_res / len(famous_people) * 100, 1)}%)")
        false_res = len(famous_people) - true_res
        print(f"Не Верно - {false_res} ({round(false_res / len(famous_people) * 100, 1)}%)")

        if false_res == 0:
            rest_val = input(f"Вы все угадали! Хотите попробовать еще раз? (введите - да)")
        else:
            rest_val = input(f"Попробуем еще раз? (введите - да)")

        if rest_val.lower() in ["da", "да"]:
            restart = True
        else:
            restart = False


