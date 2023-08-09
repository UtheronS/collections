import re
from collections import Counter

# ----------------------------------------------------------------------------------------------------------------

"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
 В результирующем списке не должно быть дубликатов. на входе [1,2,3,1,2,5,6] , на выходе [1,2]"""

# ----------------------------------------------------------------------------------------------------------------

from random import randint

# генерируем список с повторяющимися элементами
dupl_list = [randint(1, 6) for _ in range(10)]
print(dupl_list)

# создаем список, в котором не будет дупликатов
undupl_set = set()
# список с дупликатами
duplicates = []

# пробегаемся по списку
for i in dupl_list:
    # если элемента списка нет в множестве
    if i not in undupl_set:
        # то добавляем
        undupl_set.add(i)
        # иначе
    else:
        # если элемент уже есть в множестве, то добавляем в список
        duplicates.append(i)

# выводим, удаляя дубликаты с помощью set()
print(list(set(duplicates)))

# ----------------------------------------------------------------------------------------------------------------

""" В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку."""

# ----------------------------------------------------------------------------------------------------------------

# Большая строка с текстом

large_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
             "Quisque mollis iaculis condimentum. " \
             "Nunc varius, augue non malesuada efficitur, " \
             "nisl mauris vulputate urna, ut consectetur eros lorem a ex. " \
             "Cras posuere felis nisi, id pellentesque nunc sagittis at. " \
             "Nam libero velit, molestie ut faucibus quis, placerat aliquam nunc. " \
             "Cras ac purus cursus, pharetra risus vitae, consectetur nunc. " \
             "Cras quam tortor, rutrum laoreet orci vel, interdum commodo nulla. " \
             "Nunc vitae odio aliquam, tincidunt lectus eu, tempor lacus. " \
             "Sed malesuada dui in orci bibendum lacinia. Vestibulum condimentum urna erat, " \
             "a consectetur ligula maximus vel. Nunc eget semper nunc. Donec vitae dictum augue. Proin."

# С помощью re.sub мы удаляем с large_text знаки препинания, заменяем на пустое место -> ''
# и приводим весь текст к нижнему регистру
clean_text = re.sub(r'[^\w\s]', '', large_text.lower())

# Разбиваем каждое слово в список
list_words = clean_text.split()

# С помощью функции Counter мы подсчитываем вхождения(то есть сколько данных слов есть в списке) и в качестве результата
# Counter дает словарь, где ключ - слово, значение - это вхождения. Например, слово 'lorem' в списке присутствует 2 раза
# значит в словаре будет 'lorem': 2 и тд
words_counts = Counter(list_words)

# И теперь выбираем 10 самых частых вхождений
common_words = words_counts.most_common(10)

# Пробегаемся и выводим эти значения
for word, count in common_words:
    print(f"{word}: {count}")

# ----------------------------------------------------------------------------------------------------------------

""" Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. Верните все возможные варианты комплектации рюкзака. """

# ----------------------------------------------------------------------------------------------------------------
