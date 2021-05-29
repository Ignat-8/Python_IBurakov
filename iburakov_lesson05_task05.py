# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


def list_to_dict(src):
    """Формирует словарь чисел с подсчетом их повторений в заданном списке src"""
    return_dict = {}
    for num in src:
        return_dict.setdefault(num, 0)
        return_dict[num] += 1
    return return_dict


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_dic = list_to_dict(src)
result = [el for el in result_dic if result_dic[el] == 1]
print(result)
