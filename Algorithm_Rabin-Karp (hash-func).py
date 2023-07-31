def hash_full(s):
    x_temp = 1
    hash_pattern = 0
    for i in pattern:
        hash_pattern = (hash_pattern + ord(i) * x_temp) % p
        x_temp *= x
    return hash_pattern, x_temp

def hash_window(s):
    pass

if __name__ == '__main__':
    str_full = input("Введите исходную строку: ")
    pattern = input("Введите паттерн: ")

    p = 1000000007
    x = 263
    hashes = []

    hash_pattern, x_p1 = hash_full(pattern)
    hash_temp,_ = hash_full(str_full[len(str_full)-len(pattern)])
    for i in range(len(str_full)-len(pattern)-1, -1, -1):

