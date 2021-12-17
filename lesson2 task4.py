lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in lst:
    job_name = element.split(' ')[::-1]
    first_el = job_name[0]
    name = first_el.lower().title()
    print('Привет', name + "!")
