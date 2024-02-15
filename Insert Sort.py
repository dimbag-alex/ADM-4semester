s = [1000000, 1000000, 59, 29, 32, 23, 1, -1, 9, 19, 17, 31, 23, 46, 92, -1, -1, -1, -1, -1, 1000000]
#s = [3, 5, 1, 2, 4]

for i in range(1, len(s)):
    x = s[i]
    for j in range(0, i):
        if x < s[j]:
            for t in range(i, j, -1):
                s[t] = s[t - 1]
            s[j] = x
            break
print(s)
