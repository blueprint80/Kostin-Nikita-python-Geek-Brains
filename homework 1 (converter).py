duration = int(input())
dividers = [1, 60, 60, 24, 1000000]
names = ["д.", "ч.", "мин.", "сек."]
lst = []
result = []
for i in dividers:
    duration //= i
    lst.append(duration)


def func(x, y):
    return x % y


z = list(map(func, lst, dividers[1::]))[::-1]
for n in range(len(z)):
    if z[n] != 0:
        result.append(str(z[n]) + names[n])
print(" ".join(result))
