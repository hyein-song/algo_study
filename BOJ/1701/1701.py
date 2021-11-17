import sys


def kmp(sub_str):
    lens = [0 for _ in range(len(sub_str))]
    # kmp
    leng = 0
    i = 1
    while i < len(sub_str):
        if sub_str[i] == sub_str[leng]:
            leng += 1
            lens[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lens[leng - 1]
            else:
                lens[i] = 0
                i += 1
    return max(lens)


stri = sys.stdin.readline().strip()
result = 0
for i in range(len(stri)):
    result = max(kmp(stri[i:]), result)

print(result)