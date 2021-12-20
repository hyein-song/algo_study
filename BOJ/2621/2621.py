
def score():
    #숫자 연속적
    continuous = False
    tmp_cnt = 0
    for i in range(1,6):
        if num_cnt[i] == 1:
            for j in range(i, i+5):
                if num_cnt[j] == 1:
                    tmp_cnt += 1
                    continue
                else:
                    break
            break
    if tmp_cnt == 5:
        continuous = True

    #제일 큰 수
    max_num = 0
    for i in range(9, 0, -1):
        if num_cnt[i] != 0:
            max_num = i
            break

    color_cnt_sorted = sorted(color_cnt.items(), key=lambda item: item[1], reverse=True)
    num_cnt_sorted = sorted(num_cnt.items(), key=lambda item: item[1], reverse=True)

    if color_cnt_sorted[0][1] == 5:
        # 1
        if continuous:
            return max_num + 900
        # 4
        else:
            return max_num + 600

    #2
    if num_cnt_sorted[0][1] == 4:
        return num_cnt_sorted[0][0] + 800
    #3
    if num_cnt_sorted[0][1] == 3:
        if num_cnt_sorted[1][1] == 2:
            return num_cnt_sorted[0][0]*10 + num_cnt_sorted[1][0] + 700
        else:
            return num_cnt_sorted[0][0] + 400

    # 5
    if continuous:
        return max_num + 500

    if num_cnt_sorted[0][1] == 2:
        #7
        if num_cnt_sorted[1][1] == 2:
            big_num = max(num_cnt_sorted[0][0],num_cnt_sorted[1][0])
            small_num = min(num_cnt_sorted[0][0],num_cnt_sorted[1][0])
            return big_num * 10 + small_num + 300
        # 8
        else:
            return num_cnt_sorted[0][0] + 200
    # 9
    return max_num + 100


color = {'R':0,'B':1,'Y':2,'G':3}
color_cnt = {i:0 for i in range(4)}
num_cnt = {i:0 for i in range(1,10)}

for _ in range(5):
    a, b = input().split()
    b = int(b)
    color_cnt[color[a]] += 1
    num_cnt[b] += 1

print(score())