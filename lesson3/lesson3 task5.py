def get_jokes(n, double=False):
    from random import choice, shuffle
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    lst = []
    if double:
        for word_1 in nouns:
            for word_2 in adverbs:
                for word_3 in adjectives:
                    lst.append(f'{word_1} {word_2} {word_3}')
        shuffle(lst)
        return lst[:n]
    else:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for i in range(n)]


print(get_jokes(5, double=True))
print(get_jokes(5))
