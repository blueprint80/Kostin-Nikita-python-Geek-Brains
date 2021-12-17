def num_translate(en):
    n = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
         'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    for key in n:
        if en == key or en == key.title():
            if en == key.title():
                return n[key].title()
            else:
                return n[key]


num = input()
print(num_translate(num))
