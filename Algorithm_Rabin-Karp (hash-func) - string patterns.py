def hash_full(s):
    x_temp = 1
    hash_pattern = 0
    for i in s:
        hash_pattern = (hash_pattern + ord(i) * x_temp) % p
        x_temp *= x
    return hash_pattern, x_temp/x


if __name__ == '__main__':
    str_full = input("Введите исходную строку: ")
    pattern = input("Введите паттерн: ")

    p = 1000000007
    x = 263
    hashes = []
    comp = []

    hash_pattern, x_p1 = hash_full(pattern)
    hash_temp, _ = hash_full(str_full[len(str_full) - len(pattern):])
    hashes.append(hash_temp)
    for i in range(len(str_full) - len(pattern) - 1, -1, -1):
        new_hash = ((hashes[0] - ord(str_full[i + len(pattern)]) * x_p1) * x + ord(str_full[i])) % p
        hashes.insert(0, new_hash)
    for num, i in enumerate(hashes):
        if i == hash_pattern:
            chk = True
            for sim in range(len(pattern)):
                if pattern[sim] != str_full[num + sim]:
                    chk = False
            if chk:
                comp.append(num)
    print(comp)