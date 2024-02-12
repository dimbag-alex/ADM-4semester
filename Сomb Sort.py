# сортировка расческой
s = [1000000, 1000000, 59, 29, 32, 23, 1, -1, 9, 19, 17, 31, 23, 46, 92, -1, -1, -1, -1, -1, 1000000]
divider = 1.247
n = len(s) / divider

while n > 1:
    nrounded = round(n)
    for j in range(0, len(s) - nrounded):
        if s[j] > s[j + nrounded]:
            s[j], s[j + nrounded] = s[j + nrounded], s[j]
    n /= divider

print(s)

