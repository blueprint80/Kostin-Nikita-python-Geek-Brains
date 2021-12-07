cubes_odd = []
result = 0
for number in range(50):
    if number % 2 != 0:
        cubes_odd.append(number ** 3)
print(cubes_odd)

cubes_odd_add_seventeen = list(map(lambda x: x + 17, cubes_odd))

for element in cubes_odd:
    inx = cubes_odd.index(element)
    length = 0
    sum_el = 0
    while cubes_odd[inx] > 0:
        a = cubes_odd[inx] % 10
        cubes_odd[inx] //= 10
        length += 1
        sum_el += a
    if sum_el % 7 == 0:
        result += element
print(result)

print(cubes_odd_add_seventeen)

for element in cubes_odd_add_seventeen:
    inx = cubes_odd_add_seventeen.index(element)
    length = 0
    sum_el = 0
    while cubes_odd_add_seventeen[inx] > 0:
        a = cubes_odd_add_seventeen[inx] % 10
        cubes_odd_add_seventeen[inx] //= 10
        length += 1
        sum_el += a
    if sum_el % 7 == 0:
        result += element
print(result)
