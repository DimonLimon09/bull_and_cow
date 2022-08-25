import random

def bulls_and_cows(num_1, num_2):
    bulls = 0
    cows = 0
    for iteam in range(4):
        if num_1[iteam] == num_2[iteam]:
            bulls += 1
        elif num_1[iteam] in num_2:
            cows += 1
    return print(f'Число {num_1} содержит {bulls} быков и {cows} коров!')

def runner():
    user_num = input('Введите четырехзначное число: ')
    def random_number():
        ran_num = str(random.randint(1000, 10000))
        if ran_num[0] != ran_num[1] and ran_num[0] != ran_num[2] and ran_num[0] != ran_num[3] and ran_num[1] != ran_num[2] and ran_num[1] != ran_num[3] and ran_num[2] != ran_num[3]:
            print(user_num, ran_num) # Прописать вызов функции игры
            bulls_and_cows(user_num, ran_num)
        else:
            return random_number()

    if len(user_num) >= 5:    # Проверка числа
        print('Вы ввели не четырехзначное число!')
        return runner()
    if user_num[0] != user_num[1] and user_num[2] != user_num[0] and user_num[0] != user_num[3] and user_num[1] != user_num[2] and user_num[1] != user_num[3] and user_num[2] != user_num[3]:
        random_number()
    else:
        print('Число не подходит!')
        return runner()


runner()

