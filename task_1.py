# Подготовка входных данных ------------------------------------------------
duration = 0
while duration <= 0:
    duration = int(input("Введите продолжительность времени в секундах:"))
    if duration < 0:
        print("число должно быть больше нуля")
# Расчет промежутков времени -----------------------------------------------
format_out = ['сек.', 'мин.', 'час.', 'дн.', 'лет']
denominators = [60, 60, 24, 365]
list_out = [] #список выходных данных

for i in range(len(format_out)):
    if duration > 0:
        if i < len(format_out)-1:
            list_out.append([str(duration % denominators[i]), format_out[i]])
            duration = duration // denominators[i]
        else:
            list_out.append([str(duration), format_out[i]])
# Подготовка выходного сообщения -----------------------------------------
message_out = ""
len_list_out = len(list_out) - 1
for i in range(len_list_out + 1):
    message_out += list_out[len_list_out - i][0] + " " + list_out[len_list_out - i][1] + " "
#-------------------------------------------------------------------------
print(message_out)
