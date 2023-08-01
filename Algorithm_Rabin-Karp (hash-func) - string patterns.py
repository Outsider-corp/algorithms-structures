def hash_full(s):
    hash_pattern = 0
    for num, i in enumerate(s):
        hash_pattern = (hash_pattern % p + ord(i) * xes[num] % p) % p
    return hash_pattern


def find_x(x, n):
    x_temp = 1
    xes = [x_temp]
    for _ in range(n - 1):
        x_temp *= x
        xes.append(x_temp % p)
    return xes


if __name__ == '__main__':
    str_full = input("Введите исходную строку: ")
    pattern = input("Введите паттерн: ")

    p = 1000000007
    x = 263
    comp = []
    xes = find_x(x, len(pattern))
    x_p1 = xes[-1]
    hash_pattern = hash_full(pattern)
    new_hash = hash_full(str_full[len(str_full) - len(pattern):])
    if new_hash == hash_pattern:
        if pattern == str_full[len(str_full) - len(pattern):]:
            comp.append(len(str_full) - len(pattern))
    for i in range(len(str_full) - len(pattern) - 1, -1, -1):
        new_hash = ((new_hash - ord(str_full[i + len(pattern)]) * x_p1 % p) * x % p + ord(str_full[i]) % p) % p
        if new_hash == hash_pattern:
            if pattern == str_full[i:i + len(pattern)]:
                comp.append(i)
    print(" ".join(list(map(str, comp[::-1]))))
