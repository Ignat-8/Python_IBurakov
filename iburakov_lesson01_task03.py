#---------------------------------------------------------------------------
# Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 —
# получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки
#----------------------------------------------------------------------------

max_number = 20
number = 0
while True:
    number = int(input("Введите число % от 0 до " + str(max_number) + " : "))
    if number < 0:
        print("число должно быть больше 0")
    elif number > max_number:
        print("число должно быть меньше или равно " + str(max_number))
    elif 0 <= number <= max_number:
        break
#-------------------------------------------------------

message_out = []
for i in range(max_number + 1):
    if i == 1:
        message_out.append(str(i) + " процент")
    elif i > 1 and i <= 4:
        message_out.append(str(i) + " процента")
    elif (i >= 5 and i <= max_number) or i == 0:
        message_out.append(str(i) + " процентов")

# Вывод данных ---------------------------------------------------------
print(message_out[number])
print()
print('весь список склонений:')
for i, msg in enumerate(message_out):
    print(msg)

