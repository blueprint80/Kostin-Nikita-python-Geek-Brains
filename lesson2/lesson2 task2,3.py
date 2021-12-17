text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
inx = 0
while inx < len(text):
    element = text[inx]
    if any([i in '1234567890' for i in element]):
        if True:
            text.insert(inx, '"')
            text.insert(inx + 2, '"')
            text.remove(element)
            a = 0
            if 0 < int(element) < 10:
                a = '0' + element
            elif int(element) >= 10:
                a = element
            if element.startswith('+'):  # в этом блоке if добавлена возможность поменять число '+5' в списке на любое
                # двух- , трех- и т.д. значное число
                if int(element) < 10:
                    a = '+0' + element[1]
                elif int(element) >= 10:
                    a = element
            if element.startswith('-'):  # в этом блоке if добавлена возможность поменять знак '+' в списке на '-'
                if int(element) > -10:
                    a = '-0' + element[1]
                elif int(element) <= -10:
                    a = element

            inx += 1
            text.insert(inx, a)
    inx += 1
print(text)
res = " ".join(text)
print(res)
res2 = ''
i = 0
while i < len(res):
    if res[i] == '"' and res[i + 1] == ' ' and res[i + 2] in '1234567890+-':
        res2 += '"'
        i += 1
    elif res[i] == '"' and res[i - 1] == ' ' and res[i - 2].isdigit():
        res2 = res2[:-1] + '"'
    else:
        res2 += res[i]
    i += 1
print(res2)
