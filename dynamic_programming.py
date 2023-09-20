"""
Для решения задач методом динамического программирования нужно сформулировать рекуррентную задачу.
Рассматриваем последний шаг: как можно попасть в целевой случай? Обычно для этого нужно решить аналогичную задачу
для предыдущих ситуаций. Таким образом, нужно вывести формулу, которая будет вычислять значение для текущего случая
по предыдущим. А первые случаи задаются вручную как краевые ситуации.
"""


def fibonachi_numbers(n):
    """
    Функция ищет n-ное число Фибоначчи
    Рекуррентная задача:
        fibs(n) = fibs(n-1)+fibs(n-2),
        при этом fibs(0) = 0, fibs(1) = 1.
    :param n: int - номер искомого числа Фибоначчи
    :return: int - значение числа.
    """
    fibs = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]


def trajectory_count(n: int, blocked: list):
    """
    Кузнечику нужно достичь точки n. Начинает прыгать он из точки 1. Сколько способов это сделать существует,
    если он может прыгать на следующую точку и через одну (+1, +2). При этом есть заблокированные точки,
    которые указаны в списке blocked.
    Рекуррентная задача:
        count(n) = count(n-1) + count(n-2),
        при этом count(0) = 0, count(1) = 1, на каждом шаге также проверяется, не является ли точка заблокированной:
        Если является, тогда количество способов в неё попасть равно 0.
    :param n: int - конечная точка
    :param blocked: list - список заблокированных точек
    :return: int - количество способов достигнуть конечной точки.
    """
    counts = [0, 1] + [0] * (n - 1)
    counts[2] = 0 if 2 in blocked else 1
    for i in range(3, n + 1):
        if i not in blocked:
            counts[i] = counts[i - 2] + counts[i - 1]
    return counts[n]


def count_min_cost(n: int, prices: list):
    """
    Вычисляет минимальную стоимость перемещения из точки 0 в точку n-1. Посещение каждой точки имеет свою цену,
    которая указана в списке prices.
    Рекуррентная задача:
        costs(n) = prices[n] + min(costs(n-2), costs(n-1)),
        при этом costs(0) = price[0], costs(1) = price[0] + price[1].
    :param n: int - конечная точка
    :param prices: list - список стоимостей посещения точек
    :return: float - минимальная стоимость.
    """
    costs = [prices[0], prices[0] + prices[1]] + [0] * (n - 2)
    for i in range(2, n):
        costs[i] = prices[i] + min(costs[i - 2], costs[i - 1])
    return costs[n - 1]


def chess_king(m: int, n: int):
    """
    Шахматный король расположен в ячейке 1, 1. Ему нужно попасть в ячейку m, n. Король имеет право ходить только
    вниз, вправо и по диагонали вниз вправо. Сколько существует способов это сделать?
    Рекуррентная задача:
        count(m, n) = count(m-1,n) + count(m, n-1) + count(m-1, n-1),
        при этом введём фиктивные столбец и строку 0, 0, заполненные нулями,
        а также count(1,1) = 1.
    :param m: int - номер столбца конечной клетки
    :param n: int - номер строки конечной клетки
    :return: int - количество способов.
    """
    count = [[0] * (m + 1) for _ in range(n + 1)]
    count[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            count[i][j] = count[i - 1][j] + count[i][j - 1] + count[i - 1][j - 1]
    return count[n][m]


def lcs(a: list, b: list):
    """
    Поиск наибольшей общей подпоследовательности в двух списках. Для этого заполняется таблица max_ss
    размером len(a), len(b), в которой отображаются длины максимальных подпоследовательностей,
    начиная сначала.
    Рекуррентная задача:
        max_ss(i, j) = {1+max_ss(i-1, j-1), если a[i] == b[j],
                   max(max_ss(i-1, j), max_ss(i, j-1)), если a[i] != b[j]}
    :param a: list - первый список
    :param b: list - второй список
    :return: list - общая подпоследовательность.
    """
    max_ss = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                max_ss[i][j] = 1 + max_ss[i - 1][j - 1]
            else:
                max_ss[i][j] = max(max_ss[i - 1][j], max_ss[i][j - 1])

    # Восстановление подпоследовательности (проходим таблицу max_ss с конца,
    # если значение в ячейке равно одному из соседних, тогда просто уменьшаем соответствующий индекс, иначе
    # добавляем в подпоследовательность символ и уменьшаем оба индекса)
    i = len(a)
    j = len(b)
    subsequence = [0] * max_ss[-1][-1]
    while i or j:
        if max_ss[i][j] == max_ss[i - 1][j]:
            i -= 1
        elif max_ss[i][j] == max_ss[i][j - 1]:
            j -= 1
        else:
            subsequence[max_ss[i][j] - 1] = a[i - 1] if i else b[j - 1]
            i -= 1
            j -= 1
    return subsequence


def gis_len(a: list):
    """
    Поиск наибольшей возрастающей подпоследовательности в массиве a.
    Рекуррентная задача:
        gis_list(i) = {gis_list(i-1)+1, если a[i]>a[i-1],
                       gis_list(i-1), в противном случае
    :param a: list - массив, в котором ищется подпоследовательность
    :return: list - искомая подпоследовательсность.
    """
    gis_list = [0] * (len(a))
    # Выбираем следующий элемент массива
    for i in range(len(a)):
        # Проходимся по элементам подмассива и сравниваем его значения со следующим за подмассивом элементом i,
        # а также больше ли подпоследовательность того элемента среди всех в данном подмассиве
        for j in range(i):
            if a[i] > a[j] and gis_list[j] > gis_list[i]:
                gis_list[i] = gis_list[j]
        gis_list[i] += 1
    return max(gis_list)


def levenstein(a: str, b: str):
    """
    Нахождение минимального редакционного расстояния между двумя строками. Редакционное расстрояние - количество
    ошибок, которые нужно исправить для того, чтобы строки совпали.
    Варианты ошибок:
        1) Добавление символа
        2) Удаление символа
        3) Замена символа
    :param a: str - изначальная строка
    :param b: str - конечная строка
    :return: int - минимальное редакционное расстрояние.
    """
    red = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                red[i][j] = red[i - 1][j - 1]
            else:
                red[i][j] = 1 + min(red[i - 1][j], red[i][j - 1], red[i - 1][j - 1])
    return red[len(a)][len(b)]


def kmp(s: str, subs: str = '') -> bool:
    """
    Ищет подстроку subs в строке s.

    :param s: str - начальная строка
    :param subs: str - искомая подстрока
    :return: bool - найдена ли подстрока в строке
    """
    s = subs + '#' + s

    pi_f = [0] * len(s)
    j = 0
    i = 1
    while i < len(s):
        if s[j] != s[i]:
            if not j:
                pi_f[i] = 0
            else:
                j = pi_f[i - 1]
        else:
            j += 1
            pi_f[i] = j
            if j == len(subs):
                return True
        i += 1
    return False


if __name__ == '__main__':
    # n = int(input("n: "))
    # print(fibonachi_numbers(n))
    # blocked = list(map(int, input("blocked: ").split()))
    # print(trajectory_count(n, blocked))
    # prices = list(map(int, input(f"prices ({n} numbers): ").split()))
    # print(count_min_cost(n, prices))
    # m = int(input("m: "))
    # print(chess_king(m, n))
    # a = [int(i) for i in input("a: ").split()]
    # b = [int(i) for i in input("b: ").split()]
    # print(lcs(a, b))
    # print(gis_len(a))
    a = input()
    b = input()
    # print(levenstein(a, b))
    print(kmp(a, b))
