def insert_sort(array):
    """
    Сортировка вставками (O(n^2)). Постепенно увеличиваем размер упорядоченного массива.
    Сначала массив из 1 элемента, потом из 2 и так до конца.
    На каждом шаге вставляется один элемент и передвигаясь справа налево ищет своё место
    :param array: list
    """
    for n in range(1, len(array)):
        last = n
        while last > 0 and array[last] < array[last - 1]:
            array[last - 1], array[last] = array[last], array[last - 1]
            last -= 1


def choise_sort(array):
    """
    Сортировка выбором (O(n^2)). Сначала ищем минимальный элемент и ставим его на первое место.
    Затем также анализируем массив со второго элемента до конца.
    Постепенно элементы будут выстраиваться по возрастанию
    :param array: list
    """
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def bubble_sort(array):
    """
    Сортировка пузырьком (O(n^2)). Сравниваем попарно соседние элементы.
    В результате одной проходки всплывает в конец самый большой элемент
    :param array:list
    """
    for i in range(1, len(array)):
        swap = False
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break


def count_sort(array):
    """
    Сортировка подсчётом (O(n)). Проходим массив один раз и в список со счётчиками записываем,
     сколько раз встретились числа
    :param array: list
    """
    frequency = [0] * 10
    for i in array:
        if isinstance(i, int) and 0 <= i < 10:
            frequency[i] += 1
        else:
            return
    new_arr = []
    for i, num in enumerate(frequency):
        new_arr.extend([i]*num)
    for i in range(len(array)):
        array[i] = new_arr[i]

def test_sort(sort_algorithm, array, num_test):
    """
    Тест для функций сортировки
    :param sort_algorithm: func - алгоритм сортировки
    :param array: list - список для сортировки
    :param num_test: int - номер теста
    :return:
    """
    test_arr = array[:]
    sort_arr = sorted(test_arr)
    sort_algorithm(test_arr)
    print(f'testcase #{num_test}: {sort_algorithm.__name__} - {"ok" if test_arr == sort_arr else "fail"}')


if __name__ == '__main__':
    for sort in [insert_sort, choise_sort, bubble_sort, count_sort]:
        for num, arr in enumerate([[9, 1, 2, 4, 1],
                                   [0.9, 0.1, 0.5, 0.2, 0.4],
                                   list(range(4, 20)) + list(range(10))]):
            test_sort(sort, arr, num+1)
        print()
