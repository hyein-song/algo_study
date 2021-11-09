import sys


def possible_dp(s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
    dp[0][0] = 1

    for i in range(1, len_s1+1):
        dp[i][0] = dp[i-1][0] if s1[i-1] == s3[i-1] else 0
    for i in range(1,len_s2+1):
        dp[0][i] = dp[0][i-1] if s2[i-1] == s3[i-1] else 0

    for i in range(1,len_s1+1):
        for j in range(1,len_s2+1):
            if s3[i+j-1] != s1[i-1] and s3[i+j-1] != s2[j-1]:
                dp[i][j] = 0
            elif s3[i+j-1] == s1[i-1] and s3[i+j-1] == s2[j-1]:
                dp[i][j] = (dp[i-1][j] | dp[i][j-1])
            elif s3[i+j-1] == s1[i-1]:
                dp[i][j] = dp[i-1][j]
            elif s3[i+j-1] == s2[j-1]:
                dp[i][j] = dp[i][j-1]

    if dp[-1][-1]:
        return 'yes'
    else:
        return 'no'


n = int(sys.stdin.readline())
for i in range(1,n+1):
    a, b, c = sys.stdin.readline().split()
    print('Data set {}: {}'.format(i,possible_dp(a,b,c)))
