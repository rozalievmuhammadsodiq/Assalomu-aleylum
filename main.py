# 1
# from collections import namedtuple
# Sportchi = namedtuple('Sportchi', ['ismi', 'sport_turi', 'yutuqlar_soni'])
# sportchilar = [
#     Sportchi('Odilhon', 'UFS', 25),
#     Sportchi('Haaland', 'Futbolist', 20),
#     Sportchi('Azizbek', 'Boks', 10),
#
# ]
# eng_ko_p_yut_utilgan_sportchi = max(sportchilar, key=lambda x: x.yutuqlar_soni)
# print(f"Eng ko'p yutuqlarga ega sportchi: {eng_ko_p_yut_utilgan_sportchi.ismi}, "
#       f"Sport turi: {eng_ko_p_yut_utilgan_sportchi.sport_turi}, "
#       f"Yutuqlar soni: {eng_ko_p_yut_utilgan_sportchi.yutuqlar_soni}")


# 2
# numbers = [1,2,3,4,5,6]
# s = 0
# for i in numbers:
#     s += i
# print(s / len(numbers))

# 3
# numbers = range(1, 11)
# s = (x ** 2 for x in numbers)
# for i in s:
#     s.__iter__()
#     print(i)


# def kvadrat_iteratori():
#     for i in range(1, 11):
#         yield i ** 2
# for kvadrat in kvadrat_iteratori():
#     print(kvadrat)

# 4
# a = input("A: ").lower()
# s = iter(a)
# for i in a:
#     if i == "a" or i == "o" or i == "e" or i == "y" or i == "u":
#         print(f"Unlik hariflar {i}")


# 5
# def generator():
#     for i in range(1,100+1):
#         if i % 2 == 0:
#          yield i
# for i in generator():
#     print(i)


# 6
# def s():
#     def matin(a):
#         return len(a)
#     return matin
# c = s()
# print(c("Alisher Bakir"))


