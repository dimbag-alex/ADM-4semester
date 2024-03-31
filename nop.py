def longest_common_subsequence(A, B):
    n, m = len(A), len(B)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(curr[j - 1], prev[j])
        prev, curr = curr, prev

    return prev[m]


# Пример использования:
A = "AGGTAB"
B = "GXTXAYB"
result = longest_common_subsequence(A, B)
print(f"Длина НОП: {result}")
