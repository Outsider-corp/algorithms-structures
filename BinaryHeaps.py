import sys

# Подаём на вход массив значений, преобразуем его в список с целочисленными значениями
inp = list(sys.stdin)
arr = list(map(int, inp[0].split()))


class MaxHeap:

    def __init__(self, arr):
        self.parents = arr
        self.create_heap()

    # Создание бинарной кучи
    def create_heap(self):
        pass

    # Добавление значения (приоритета) в кучу
    def insert(self, p):
        pass

    # Извлечение максимального элемента (корня)
    def extract_max(self):
        pass

    # Удаление элемента из кучи
    def remove(self, p):
        pass

    # Изменение приоритета элемента i на приоритет p
    def change_priority(self, i, p):
        pass
