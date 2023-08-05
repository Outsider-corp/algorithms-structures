"""
Исходим из краевого случая: у нас один диск. Тогда мы его перекладываем из origin на destination.
Если у нас больше одного диска, тогда мы все, кроме песледнего, перекладываем на temp, потом последней диск кладём
на destination, и перемещаем всю башню из temp на destination.
"""

def hanoi_instructions(h, origin, destination, temp):
    """
    Функция, которая даёт инструкции для игры Ханойские башни
    :param h: int - высота башни
    :param origin: int - номер начальной башни
    :param destination: int - номер конечной башни
    :param temp: int - номер временной башни
    """
    if h < 2:
        print(f"Move disk 1 from {origin} rod to {destination} rod.")
    else:
        hanoi_instructions(h - 1, origin, temp, destination)
        print(f"Move disk {h} from {origin} rod to {destination} rod.")
        hanoi_instructions(h - 1, temp, destination, origin)


if __name__ == '__main__':
    h = int(input())
    hanoi_instructions(h, 1, 2, 3)
