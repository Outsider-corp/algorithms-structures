def generate_number(n: int, m: int, prefix=None):
    """
    Функция, которая генерирует все числа в n-ричной системе счисления длины m
    :param n: int - основание системы счисления
    :param m: int - размер нужной (оставшейся) строки
    :param prefix: list - список цифр в текущей последовательности
    """
    if m == 0:
        print(*prefix, sep="")
        return
    prefix = prefix or []
    for number in range(n):
        prefix.append(number)
        generate_number(n, m - 1, prefix)
        prefix.pop()


def generate_permutations(n: int, m: int = -1, prefix=None):
    """
    Функция, которая генерирует все перестановки n чисел в m позициях
    :param n: int - количество цифр (наибольшее число)
    :param m: int - количество ячеек
    :param prefix: list - список цифр в текущей последовательности
    """
    m = m if m != -1 else n
    if m == 0:
        print(*prefix, sep="")
        return
    prefix = prefix or []
    for number in range(1, n+1):
        if number not in prefix:
            prefix.append(number)
            generate_permutations(n, m - 1, prefix)
            prefix.pop()


if __name__ == '__main__':
    type_task = int(input("Введите задачу, которую хотите запустить "
                          "(1 - все числа системы n, 2 - перестановки):"))
    if type_task == 1:
        n = int(input("Введите основание системы: "))
        m = int(input("Введите длину чисел: "))
        generate_number(n, m)
    elif type_task == 2:
        n = int(input("Введите максимальное число: "))
        m = int(input("Введите количество ячеек (0 - если длина равна n): "))
        generate_permutations(n, m if m != 0 else n)
