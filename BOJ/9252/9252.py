
def dp(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    table = [['' for _ in range(len_s2+1)] for _ in range(len_s1+1)]
    for i in range(1, len_s1+1):
        for j in range(1, len_s2+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + s1[i-1]
            else:
                if len(table[i-1][j]) >= len(table[i][j-1]):
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i][j-1]

    if table[-1][-1] == '':
        print(0)
    else:
        print(len(table[-1][-1]))
        print(table[-1][-1])


s1 = input()
s2 = input()
dp(s1,s2)
