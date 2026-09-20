# if __name__ == '__main__':
#     n = int(input())
#     famous = [0 for _ in range(n)]
#     fr = [list(map(lambda x: 1 if x=='Y' else 0,input())) for i in range(n)]
#     # print('\n'.join(map(str, fr)))
    
#     for i in range(len(fr)):
#         for j in range(len(fr[i])):
#             if fr[i][j]:
#                 famous[i] += sum(fr[j])

#     print(max(famous))
#     # print(famous)

# 갈아엎음

n = int(input())
friends = [list(input()) for _ in range(n)]

connected = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[k][i] == "Y" and friends[j][k] == "Y"):
                # 수식을 꼭 이렇게 해야 하나? 너무 어려운 것 같은디
                connected[i][j] = 1

answer = 0
for row in connected:
    answer = max(answer, sum(row))
print(answer)