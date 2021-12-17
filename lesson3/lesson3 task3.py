NAMES = ("Иван", "Мария", "Петр", "Илья", "Георгий", "Екатерина", "Николай", "Александр", "Ирина", "Григорий",
         "Евгений", "Нина", "Святослав", "Вероника", "Дарья", "Дмитрий", "Владимир", "Игорь", "Егор", "Сергей")


def thesaurus(names):
    lst = []
    first_letter = []
    buffer = []
    my_dict = {}
    letter_count = 0
    for name in names:
        first_letter.append(name[0])
        lst.append(name)
        lst.sort()
    first_letter.sort()
    for name, letter in zip(lst, first_letter):
        if first_letter.count(letter) > 1:
            buffer.append(name)
            my_dict[letter] = buffer.copy()
            letter_count += 1
            if first_letter.index(letter) != lst.index(name) and first_letter.count(letter) == letter_count:
                buffer.clear()
                letter_count = 0
        else:
            my_dict[letter] = [name]
    return my_dict


print(thesaurus(NAMES))
