# 1-misol
# sum = 0
# n = int(input('.... '))
# for x in range(1, n+1):
#   if x % 2 == 0:
#     sum += -x
#   else:
#     sum += x
#   print(sum)

# 2-misol
# n = int(input('.... '))
# for x in range(1, n):
#   if n % x == 0:
#     print(x, end=', ')

# 3-misol
faylnomi = 'new_file.txt'
number1 = '919328932'
number2 = '993243234'
with open(faylnomi, 'a') as fayl:
  fayl.write(number1 + '\n')
  fayl.write(number2 + '\n')
with open(faylnomi) as fayl:
  for num in fayl:
    print(f"+998{num}")

# 4-misol
# Point nomli class yarating.Point a list tipli argumentni qabul qiladi.max_son nomli metod tuzish kerak,metodni vazifasi a argumentni ichidagi
# qiymatlarning eng kattasini chiqarishdan iborat(max funksiyasidan foydalanmagan holda),metodga max_son() emas max_son deb murojat qlish imkoni bo'lsin(30 ball)

# class Point():
#   def __init__(self, a):
#     self.a = a
#   @property
#   def get_sort(self):
#     for x in range(len(self.a)):
#       min_index = x
#       for j in range(x+1, len(self.a)):
#         if self.a[min_index] < self.a[j]:
#           min_index = j
#       if self.a[x] != self.a[min_index]:
#         self.a[x], self.a[min_index] = self.a[min_index], self.a[x]
#     return self.a
#   @property
#   def get_max(self):
#     return self.a[0]

# a = Point([3, 19, 110, 1])
# print(a.get_sort)
# print(a.get_max)

# 5-misol
# Yil chiroyli hisoblanadi, agarda uning barcha raqamlari har hil bo'lsa.Yilning chiroyli yil ekanligini tekshirish kerak(20 ball)

# izoh:
# 2013 -chiroyli yil
# 202- chiroyli yil emas

# n = int(input('yil..... '))
# k = n
# sum = []
# while n!=0:
#   m = n % 10
#   sum.append(m)
#   n = n // 10
# count = 0
# for x in sum:
#   if sum.count(x) > 1:
#     count += 2
# if count > 1:
#   print(k, ' chroyli yil emas')
# else: print(k, ' chroyli yil ')

# 6-masala
# Inson nomli class tuzing.Class ikki argumentni qabul qiladi:age va maosh. karra_argument nomli metod tuzing.
# Metodning vazifasi maosh age dan necha marta katta ekanini chiqarish(20 ball)

# class Inson():
#   def __init__(self, age, maosh) -> None:
#     self.age = age
#     self.maosh = maosh
#   def marta_katta(self):
#     return self.maosh // self.age
#   def __lt__(self, boshqa):
#     return self.age < boshqa.age

# person1 = Inson(18, 4800)
# person2 = Inson(21, 2456)
# print(person1.marta_katta())
# print(person1<person2)


# 7-masala
# s satr berilgan shu satrning ichidagi sonlarni raqamlar yig'indisini ekranga chiqaring(15 ball):
# s = input('s... ')
# digit_count = 0
# for x in s:
#   if x.isdigit():
#     digit_count += int(x)
# print(digit_count)

# 8-masala
# Sizga n ta son berilgan bo'lib, sizning vazifangiz shulardan 0 ga eng yaqinini topishdan iborat.(15 ball)
# n = list(map(int, input('..... ').split()))
n = [2, 3, 4, -5, -1]
# noldan_katta = []
# noldan_kichik = []
# for x in n:
#   if x>0:
#     noldan_katta.append(x)
#   else: noldan_kichik.append(x)
# katta = (min(noldan_katta))   # 3
# kichik = (max(noldan_kichik))   # -1
# n_katta = abs(katta-0)    # 3
# n_kichik = abs(kichik-0)   # -1 => 1

# if n_katta>n_kichik:   # 3 > 1
#   print(kichik, ' yaqin 0 ga ')
# elif n_katta<n_kichik:
#   print(katta, ' yaqin 0 ga ')
# else: print('ikkovi bir xil yaqin')

