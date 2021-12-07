for number in range(101):
    if number % 10 == 1 and number not in range(10, 21):
        print(number, "процент")
    elif number % 10 == 2 and number not in range(10, 21):
        print(number, "процента")
    elif number % 10 == 3 and number not in range(10, 21):
        print(number, "процента")
    elif number % 10 == 4 and number not in range(10, 21):
        print(number, "процента")
    else:
        print(number, "процентов")
