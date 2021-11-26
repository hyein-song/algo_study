import math

mod = 1000000007

# 거듭제곱 빠르게 구하기
def pow(a,b):
    if b == 0:
        return 1
    if b % 2 > 0: # 홀수
        return (pow(a,b-1)*a) % mod
    # 짝수
    h = pow(a,b//2)
    return (h*h)%mod


# 페르마의 정리로 분모를 거듭제곱 형태로 변경해줌
def binomial(n, k):
    a = 1
    b = 1
    # n!
    for i in range(1,n+1):
        a *= i
        a %= mod
    # k!
    for i in range(1,k+1):
        b *= i
        b %= mod
    # n-k!
    for i in range(1,n-k+1):
        b *= i
        b %= mod
    b = pow(b,mod-2) % mod
    result = a * b % mod
    return result

n, k = map(int, input().split())
print(binomial(n, k))

# 주의할 점
# factorial, pow 계산을 내장함수를 사용하면 시간초과 발생
# 계속 mod 로 modular 해줘야 하기 때문