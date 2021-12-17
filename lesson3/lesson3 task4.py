
def thesaurus(*args):
    doubles = []
    lst = []
    dict_name = {}
    dict_result = {}
    first_letter_name = []
    first_letter_lastname = []
    for element in args:
        first_letter_name.append(element[0])
        for i in element[1::]:
            if i.istitle():
                first_letter_lastname.append(i)
    for letter_name, letter_lastname, name in zip(first_letter_name, first_letter_lastname, args):
        if first_letter_name.count(letter_name) > 1 and first_letter_lastname.count(letter_lastname) > 1:
            doubles.append(name)
            dict_name[letter_name] = doubles
            dict_result[letter_lastname] = dict_name
        elif first_letter_lastname.count(letter_lastname) > 1:
            dict_name[letter_name] = [name]
        else:
            dict_result[letter_lastname] = dict_result.fromkeys(letter_name, [name])

    list_keys = list(dict_result.keys())
    list_keys.sort()
    for i in list_keys:
        b = [i, dict_result[i]]
        lst.append(b)
    final_dict = dict(lst)
    return final_dict


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
