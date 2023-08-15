def fibonachi_numbers(n):
    """
    Функция ищет n-ное число Фибоначчи
    :param n: int - номер искомого числа Фибоначчи
    :return: int - значение числа
    """
    fibs = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]


def trajectory_count(n: int, blocked: list):
    """
    Кузнечику нужно достичь точки n. Начинает прыгать он из точки 1. Сколько способов это сделать существует,
    если он может прыгать на следующую точку и через одну (+1, +2). При этом есть заблокированные точки,
    которые указаны в списке blocked
    :param n: int - конечная точка
    :param blocked: list - список заблокированных точек
    :return: int - количество способов достигнуть конечной точки
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
    которая указана в списке prices
    :param n: int - конечная точка
    :param prices: list - список стоимостей посещения точек
    :return: float - минимальная стоимость
    """
    costs = [prices[0], prices[1]] + [0] *(n-2)
    for i in range(2, n):
        costs[i] = prices[i] + min(costs[i-2], costs[i-1])
    return costs[n-1]


if __name__ == '__main__':
    n = int(input("n: "))
    # print(fibonachi_numbers(n))
    # blocked = list(map(int, input("blocked: ").split()))
    # print(trajectory_count(n, blocked))
    prices = list(map(int, input(f"prices ({n} numbers): ").split()))
    print(count_min_cost(n, prices))
