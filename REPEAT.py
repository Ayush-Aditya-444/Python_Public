# for _ in range(int(input())):
#     a, b, c = map(int, input().split())
#     new = [i for i in range(1, (2 * a) + 1, 2)]
#     for i in range(a):
#         q = [i for i in new]
#         q.append((b - 1) * new[i])
#         if sum(q) == c:
#             print(new[i])
#             break

"""
3
3 2 14
5 4 28
2 3 10

"""

"""
5
1
3

"""

for _ in range(int(input())):
    n, k, s = map(int, input().split())
    print((s - (n * n)) // (k - 1))
