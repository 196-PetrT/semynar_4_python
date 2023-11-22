# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

text = 'a a a b c a a d c d d'
text_new = ''
text = text.split(' ')
for i in text:
    count_t = text_new.count(i)
    # print(count1)
    if text_new.count(i) == 0:
        text_new += i + ' '
    else:
        text_new += i + '_' + str(count_t) + ' '
print(text_new)


# lst = "a a a b c a a d c d d".split()
# print(lst)
# dct = {}
# for item in lst:
#     if item in dct:
#         print(f"{item}_{dct[item]}", end=' ')
#     else:
#         print(item, end=' ')
#     dct[item] = dct.get(item, 0) + 1
