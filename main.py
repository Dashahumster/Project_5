f_str = input('Введите имя файла: ')
day = int(input('Введите день, когда хотите сделать скидку: '))
percent = int(input('Введите скидку (в %): '))
try:
    with open(f_str) as f_in:
        text = f_in.readlines()
        _sum_profit = int(text[0]) #сумма за 31 день
        av_profit = _sum_profit / 31 #средняя выручка в день
        percent = (percent / 100) + 1 #процент на который увеличивается
        n_av_profit = int(text[day]) * percent #новая средняя выручка после скидки
        dif_av_profit = n_av_profit - av_profit #разница
        print('Выручка изменилась бы на: ', dif_av_profit)
except  FileNotFoundError:
    print('Файл {} не найден.'.format(f_str))
except IndexError:
    print('День {} не указан'.format(day))