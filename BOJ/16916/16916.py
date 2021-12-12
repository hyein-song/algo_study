
def kmp(a, b):
    table = [0] * (len(a) +1)

    leng = 0
    i = 1
    while i < len(b):
        if b[i] == b[leng]:
            leng += 1
            table[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = table[leng-1]
            else:
                table[i] = 0
                i += 1

    i = 0
    j = 0
    while i < len(a):
        if b[j] == a[i]:
            i += 1
            j += 1
        elif b[j] != a[i]:
            if j != 0:
                j = table[j-1]
            else:
                i += 1

        if j == len(b):
            return 1

    return 0


def rk(a,b):
    hash_b = 0
    len_b = len(b)
    for i in range(len_b):
        hash_b += (ord(b[i])*(2**(len_b-1-i)))
    # print('b',hash_b)
        hash_b %= 100000
    hash_a = 0
    for i in range(len_b):
        hash_a += (ord(a[i]) * (2 ** (len_b - 1 - i)))
        hash_a %= 100000
    if hash_b == hash_a:
        if b == a[:len_b]:
            return 1
    # print(hash_a)
    for j in range(1, len(a)-len_b):
        m = ord(a[j-1]*(2 ** (len_b - 1)))
        new_val = ord(a[j+len_b-1])
        # print(a[j+len_b-1], new_val)
        hash_a = (hash_a - m) * 2 + new_val
        hash_a %= 100000
        # print(hash_a)
        if hash_b == hash_a:
            if b == a[j:j+len_b]:
                return 1
    return 0

a = input()
b = input()

# print(kmp(list(a),list(b)))
print(rk(a,b))
print(len(b))