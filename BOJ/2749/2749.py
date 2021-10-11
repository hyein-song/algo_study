import sys

mod = 1000000
p = mod // 10 * 15
x = int(sys.stdin.readline().strip())
fib = [0,1]
for i in range(2,p):
    fib.append(fib[i-1]+fib[i-2])
    fib[i] %= mod
print(fib[x%p])

# 피사노 주기
# 피보나치 수를 k로 나눈 나머지는 항상 주기를 가지게 된다는 원리
# 주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는
# N%P번째 피보나치 수를 M을 나눈 나머지와 같다.
# M = 10k 일 때, k > 2 라면, 주기는 항상 15 × 10k-1 이다.
