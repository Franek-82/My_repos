def f_sum(li):
    if not li:
        return 0
    return li[0] + f_sum(li[1:])

print(f_sum([1, 2, 3, 4, 5]))