class DisjointSet:

    def __init__(self, num=100):
        self.parent = [-1] * num
        self.rank = [-1] * num

    # Создание множества, состоящего из одного элемента
    def make_set(self, i: int):
        self.parent[i] = i
        self.rank[i] = 0

    # Поиск корня для дерева (к какому множеству принадлежит i)
    def find(self, i: int):
        print(f"find... {i}: {self.parent[i]}")
        if i != self.parent[i]:
            # Добавлена эвристика сжатия путей: для отца вершины ищем корень и записываем его вместо отца
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Объединение двух множеств:
    # к множеству, у которого корень имеет больший ранг, подвешивается второе множество.
    # Если ранги равны, то высота основного множества увеличивается на единицу
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            # Увеличиваем ранг корня, если объединяемые множества имели равный ранг
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


if __name__ == '__main__':
    inp = input("Введите наибольшее число в множествах:")
    disjoinset = None
    try:
        disjoinset = DisjointSet(int(inp) + 1)
    except:
        print("Вы ввели не число")
    if disjoinset:
        while True:
            try:
                inp = input("...")
                if inp == "q":
                    break
                elif "find" in inp.lower():
                    num = int(inp.split()[-1])
                    if disjoinset.parent[num] != -1:
                        print(disjoinset.find(num))
                    else:
                        print("Такого значения нет в множествах")
                elif "union" in inp.lower() or "aaa" in inp.lower():
                    num1 = int(inp.split()[-1])
                    num2 = int(inp.split()[-2])
                    if disjoinset.parent[num1] != -1 and disjoinset.parent[num2] != -1:
                        disjoinset.union(num1, num2)
                        print("Множества успешно обновлены")
                    else:
                        print("Какое-либо из поданных чисел отсутствует в множествах")
                elif "eval" in inp:
                    print(eval(" ".join(inp.split()[1:])))
                elif "show" in inp.lower() or "s" in inp.lower():
                    print(disjoinset.parent)
                else:
                    if int(inp) >= len(disjoinset.parent):
                        print("Значение выходит за границы массива")
                        continue
                    elif int(inp) in disjoinset.parent:
                        print("Это значение уже присутствует в одном из множеств")
                        continue
                    disjoinset.make_set(int(inp))
            except Exception as e:
                print(f"Вы подали что-то с ошибкой... \n {e}")
