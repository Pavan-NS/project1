T = int(input())
# print(T)
while T > 0:
    T = T - 1
    a = []
    c = []
    d = []
    count1 = 0
    count2 = 0
    N, M = input().split()
    N, M = int(N), int(M)
    for i in range(N):
        b = list(input())
        # print(b)
        a = a + b
    for i in range(N):
        for j in range(M):
            if i % 2 == 0:
                if j % 2 == 0:
                    c.append("G")
                    d.append("R")
                else:
                    c.append("R")
                    d.append("G")
            else:
                if j % 2 == 0:
                    c.append("R")
                    d.append("G")
                else:
                    c.append("G")
                    d.append("R")
    for i in range(len(a)):
        # print(i)
        if a[i] != c[i]:
            if a[i] == "R":
                count1 = count1 + 5
            else:
                count1 = count1 + 3
        if a[i] != d[i]:
            if a[i] == "R":
                count2 = count2 + 5
            else:
                count2 = count2 + 3
    print(min(count1, count2))
