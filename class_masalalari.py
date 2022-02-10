# 1 - 2
# class Student:
#   def __init__(self, name, age) -> None:
#     self.name = name
#     self.age = age
#   def __str__(self) -> str:
#     return f"{self.name} {self.age} yoshda"
# talaba1 = Student('Eldor', 20)
# print(talaba1)
# 3- masala
# class Student():
#   def __init__(self, name, age) -> None:
#     self.name = name
#     self.age = age
#     self.balls = []
#   def get_average(self, ball_input):
#       self.balls.append(ball_input)
#       return [ball for ball in self.balls]

# talaba1 = Student('Samandar', 16)
# print(talaba1.get_average(42))

# 4-masala
# class Int_num():
#   def __init__(self, a, b) -> None:
#     self.a = a
#     self.b = b
#   def get_info(self):
#     return isinstance(self.a, int)

# class Number(Int_num):
#   def __str__(self) -> str:
#       return super().__str__()

# amal = Number(1.2, 4)
# print(amal.get_info())

# 5-masala
# class Number():
#   def __init__(self, n) -> None:
#       self.n = n
#   def digit_num(self):
#     sum = 0
#     while self.n:
#       m = self.n % 10
#       sum += m
#       self.n = self.n // 10
#     return sum
# amal = Number(455)
# print(amal.digit_num())

# 6-masala
# 6.Number nomli klass yarating. Class bitta argument berilsin: value. Qo'shish operatori qayta yuklansin. Metod yangi 
# Number obyektini qaytarsin. __str__ metodi qayta yuklansin. Metod value qiymatini qaytarsin.(20 ball)
# izoh:
# n = Number(5)
# m = Number(6)
# print(n + m + n) 

# class Number():
#   def __init__(self, n, m) -> None:
#     self.n = n
#     self.m = m
#   def __str__(self):
#       text = self.n + self.m + self.n
#       return str(text)
# print(Number(2, 4))

# 7-masala
# 7.Point nomli klass yaratilsin. Class ikkita argument qabul qiladi: x va y. Point uchun qo'shish, ayirish operatorlari qayta yuklansin.
#  Ko'paytirish amali qayta yuklansin. __str__ metodi qayta yuklansin.(25 ball)
# class Point():
#   def __init__(self, x):
#     self.x = x
#   def __add__(self, y):
#     return self.x + y
#   def __sub__(self, z):
#     return self.x - z
#   def __mud__(self, a):
#     return self.x * a
#   def __str__(self) -> str:
#       return self.x
# amal1 = Point(4) 
# print(amal1.__add__(3))
# print(amal1.__sub__(2))
# print(amal1.__mud__(3))
# print(Point('salom'))

# 8-masala
# 8.Person nomli klass yarating. Klass ikkita argumentni qabul qilsin: name, age. Barcha taqqoslash operatorlari qayta yuklansin. 
# Taqqoslashda yoshi  ishlatilsin.(35 ball)
# izoh:
# p1 = Person('name1', 20)
# p2 = Person('name2', 22)
# p1 < p2   # True
# p1 >= p2  # False 
class Person():
  __person_count = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.__person_count += 1
  def __repr__(self) -> str:
    return f"Avto: {self.name} {self.age} yoshda"
  def __eq__(self, boshqa_yosh) :
    return self.age == boshqa_yosh.age
  def __lt__(self, boshqa_yosh):
    return self.age<boshqa_yosh.age
  def __le__(self, boshqa_yoash):
    return self.age <= boshqa_yoash.age
  def __len__(self):
    return len(self.name)
  
person1 = Person('samandar', 16)
person2 = Person('Elbek', 20)  
print(person1==person2)
print(person2>person1)
print(person1<=person2)
print(Person.__len__(person2))

