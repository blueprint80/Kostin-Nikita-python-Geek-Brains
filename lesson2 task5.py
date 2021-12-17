prices = [56.47, 32.55, 44.6, 153.32, 32.07, 453.32, 692.08, 124, 325.50, 931.33]
print(prices)
print(id(prices))
prices_form = []
for price in prices:
    rub = round(price // 1)
    kop = round(price % 1 * 100)
    if len(str(kop)) == 1:
        kop = '0' + str(kop)
    if kop == 0:
        kop = str(kop) + '0'
    res = f'{rub} руб. {kop} коп.'
    prices_form.append(res)
print(", ".join(prices_form))
prices.sort()
print(prices)
print(id(prices))
prices_srt = []
for price in prices:
    rub = round(price // 1)
    kop = round(price % 1 * 100)
    if len(str(kop)) == 1:
        kop = '0' + str(kop)
    if kop == 0:
        kop = str(kop) + '0'
    res = f'{rub} руб. {kop} коп.'
    prices_srt.append(res)
print(", ".join(prices_srt))
prices_rev = prices_srt[::-1]
rev_prices = ", ".join(prices_rev)
print(rev_prices)
high_prices = prices_rev[:5][::-1]
print(", ".join(high_prices))
