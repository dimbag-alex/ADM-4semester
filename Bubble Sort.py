s = [1000000,1000000,59, 29, 32, 23, 1, -1, 9, 19, 17, 31, 23, 46, 92,-1,-1,-1,-1,-1, 1000000]
s1 = s
for j in range(len(s) - 1, 0, -1):
    for i in range(0, j):
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]

print(s == sorted(s1))
print(s)
