class MaxBinaryHeap:

    def __init__(self, arr):
        self.H = arr
        self.create_heap()

    @property
    def size(self):
        return len(self.H)

    # Номер родителя элемента
    @staticmethod
    def parent(i):
        return (i - 1) // 2

    # Номер левого ребёнка элемента
    @staticmethod
    def left_child(i):
        return i * 2 + 1

    # Номер правого ребёнка элемента
    @staticmethod
    def right_child(i):
        return i * 2 + 2

    # Создание бинарной кучи
    def create_heap(self):
        # Проходим по элементам от середины к началу и просеиваем их вниз
        for el in range(self.size // 2, -1, -1):
            self.sift_down(el)

    # Просеивание вершины вверх
    def sift_up(self, i):
        # Проверка, что элемент не является корнем дерева и
        # что значение элемента меньше, чем значение родителя
        while i > 0 and self.H[MaxBinaryHeap.parent(i)] < self.H[i]:
            # Меняем местами элемент родителя и текущий элемент
            self.H[MaxBinaryHeap.parent(i)], self.H[i] = self.H[i], self.H[MaxBinaryHeap.parent(i)]
            # Переходим к родителю для дальнейшей проверки
            i = MaxBinaryHeap.parent(i)

    # Просеивание вершины вниз
    def sift_down(self, i, size=None):
        # Проверка необязательного параметра size, который нужен для сортировки бинарной кучей
        if size is None:
            size = self.size
        max_index = i
        l = MaxBinaryHeap.left_child(i)
        # Проверка, что левый ребёнок существует и больше ли он текущего
        if l < size and self.H[l] > self.H[max_index]:
            max_index = l
        r = MaxBinaryHeap.right_child(i)
        # Проверка, что правый ребёнок существует и больше ли он максимального
        if r < size and self.H[r] > self.H[max_index]:
            max_index = r
        # Проверка, является ли один из сыновей больше, чем текущий элемент
        if max_index != i:
            # Меняем местами текущий элемент с ребёнком, который больше
            self.H[max_index], self.H[i] = self.H[i], self.H[max_index]
            # Снова вызываем этот метод, но уже для большего ребёнка
            # (в нём будет значение, которое просеивается)
            self.sift_down(max_index, size)

    # Добавление значения (приоритета) в кучу
    def insert(self, p):
        # Добавление элемента в конец списка
        self.H.append(p)
        # Просеивание этого элемента вверх
        self.sift_up(self.size - 1)

    # Извлечение максимального элемента (корня)
    def extract_max(self):
        # Меняем местами корень дерева с его последним листом
        self.H[0], self.H[-1] = self.H[-1], self.H[0]
        # Сохранение максимального элемента в переменную (и его удаление из кучи)
        max_el = self.H.pop(-1)
        # Просеивание элемента, находящегося в корне, вниз
        self.sift_down(0)
        return max_el

    # Удаление элемента из кучи
    def remove(self, i):
        # Присвоение элементу, который нужно удалить, бесконечного приоритета
        self.H[i] = int("inf")
        # Просеивание этого элемента вверх (перемещение его в корень)
        self.sift_up(i)
        # Извлечение максимального элемента (то есть удаление этого элемента
        self.extract_max()

    # Изменение приоритета элемента i на приоритет p
    def change_priority(self, i, p):
        # Сохраняем предыдущее значение приоритета элемента i
        old_p = self.H[i]
        # Устанавливаем новый приоритет элементу i
        self.H[i] = p
        # Проверяем, если новый приоритет больше старого, тогда просеиваем элемент вверх,
        # в противном случае просеиваем его вниз
        if p > old_p:
            self.sift_up(i)
        else:
            self.sift_down(i)

    # Сортировка бинарной кучей*
    def heap_sort(self):
        size = self.size
        # Проходим по всем элементам
        while size > 1:
            heap.H[0], heap.H[size - 1] = heap.H[size - 1], heap.H[0]
            size -= 1
            heap.sift_down(0, size)

if __name__ == '__main__':
    # Подаём на вход массив значений, преобразуем его в список с целочисленными значениями
    inp = input("Input array:")
    arr = list(map(int, inp.split()))
    heap = MaxBinaryHeap(arr)
    while True:
        inp = input()
        if inp == "q":
            break
        elif "add" in inp:
            heap.insert(int(inp.split()[-1]))
        elif "remove" in inp:
            heap.remove(int(inp.split()[-1]))
        elif "change" in inp:
            heap.change_priority(int(inp.split()[-2]), int(inp.split()[-1]))
        elif inp == "heap":
            print(heap.H)
        elif inp == "sort":
            heap.heap_sort()
        elif inp == "heap again":
            heap.create_heap()
        elif inp == "new heap":
            inp = input("Input array:")
            arr = list(map(int, inp.split()))
            heap = MaxBinaryHeap(arr)
        else:
            print("no actions.")
