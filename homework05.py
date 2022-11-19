# задание 1
# from datetime import date
#
# class Phonebook:
#     def __init__(self, ID, f_name, l_name, birth, profession):
#         self.ID = ID
#         self.f_name = f_name
#         self.l_name = l_name
#         self.birth = birth
#         self.profession = profession
#
#     def get_information(self):
#         return f'ID: {self.ID} ФИО: {self.f_name, self.l_name} Дата рождения: {self.birth} Профессия: {self.profession}'
#
# book = Phonebook(1, 'Лариса', 'Иванова', date(year=1980, month=2, day=1), 'Технолог')
# book2 = Phonebook(2, 'Иван', 'Иванов', date(year=1972, month=6, day=4), 'Сантехник')
# book3 = Phonebook(3, 'Петр', 'Зародин', date(year=1956, month=12, day=28), 'Пенсионер')
#
# print(book.get_information())
# print(book2.get_information())
# print(book3.get_information())


# задание 2
# class Bird:
#     def __init__(self, age):
#         self.age = age
#
#     def eat(self):
#         return 'I\'m eating worms!'
#
#     def fly(self):
#         return 'I believe, I can fly!'
#
# class Eagle(Bird):
#     def hunt(self):
#         return 'I wan\'t to eat some fish!'
#
# orel = Eagle(12)
# print(orel.eat(),orel.age,'years old!', orel.fly(), orel.hunt())
#
# class Penguin(Bird):
#     def fly(self):
#         return 'Я не летаю.'
#
#     def swim(self):
#         return 'Зато я плаваю!'
#
# ping = Penguin(4)
# print('Мне',ping.age,'.',ping.fly(), ping.swim())
#
#
# class Mammal:
#     def __init__(self, age):
#         self.age = age
#
#     def eat(self):
#         return 'I like to eat some herbs!'
#
#     def sleep(self):
#         return 'I wan\'t to sleep'
#
#     def hide(self):
#         return 'I\'m hidding!'
#
# class Antelope(Mammal):
#     def hide(self):
#         return 'Я в кустах'
#
# ant = Antelope(5)
# print(ant.eat(), 'I am',ant.age,'years old!', ant.hide())
#
# class Predator(Mammal):
#     def eat(self):
#         return 'И я не в кустах,и найду тебя антилопа!'
#
# lion = Predator(10)
# print('Мне', lion.age,'!',lion.eat())
#
#
# class Fish:
#     def __init__(self, age):
#         self.age = age
#
#     def swim(self):
#         return 'I love to swim!'
#
#     def eat(self):
#         return 'Я ем, что есть!'
#
# class Trout(Fish):
#     pass
#
# forel = Trout(3)
# print('Я форель!', forel.swim(), forel.eat())
#
# class Whale(Fish):
#     def eat(self):
#         return 'Я очень много ем, вы меня видели?'
#
# kit = Whale(25)
# print('А я кит.', kit.eat())



# задание 3
# def show_even_numbers(*args):
#     even_numbers_lst = []
#     for i in args:
#         try:
#             if i % 2 == 0:
#                 even_numbers_lst.append(i)
#
#         except TypeError:
#             continue
#
#     return even_numbers_lst
#
#
# def show(even):
#     count = 1
#     for i in even:
#         print(f'{count} - {i}')
#         count += 1
#
# show(show_even_numbers(33, 18, 16, 22, 20, 200, 188))