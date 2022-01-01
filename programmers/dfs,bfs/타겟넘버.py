
#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(x, result):
        nonlocal cnt
        if x == n:
            if result == target:
                cnt += 1
            return

        dfs(x + 1, result + numbers[x])
        dfs(x + 1, result - numbers[x])

    dfs(0, 0)

    return cnt
