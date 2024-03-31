# сортировка выбором:
# на каждом шаге выбираем минимум из оставшегося массива и ставим на массивом
import random
def choose_sort(m: list) -> list:
    for c in range(len(m)):
        curmin_index = c
        for elem_index in range(c, len(m)):
            if m[elem_index] < m[curmin_index]:
                curmin_index = elem_index
        m[curmin_index], m[c] = m[c], m[curmin_index]
    return m


to_be_sorted = [-1, 0, 5, 6, -3, 5, 9, 111]
print(choose_sort(to_be_sorted))

real_check = [random.randint(-1000,1000) for _ in range(1000)]
print(choose_sort(real_check) == sorted(real_check))
