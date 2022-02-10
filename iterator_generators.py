# numbers = [3, 7, 4, 3, 89]
# # for x in numbers:
# #   print(x)
# iteration = iter(numbers)
# for x in numbers:
#   print(iteration.__next__())


# def prostoy():
#   print(' 4 - ')
#   yield 4
#   print(' 5 - ')
#   yield 5
#   print(' 6- ')
#   yield 6
#   print(' 7 - ')
#   yield 7

# value = prostoy()
# print(next(value))

# def kvadrati():
#   for x in range(1, 11):
#     print(f"{x} ning kvadarati")
#     yield x**2

# value = kvadrati()
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))


# class myNums:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
# myclass = myNums()
# myit = iter(myclass)
# print(next(myit))


class myNums:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else: raise StopIteration
myclass = myNums()
myiter = iter(myclass)
for x in myiter:
  print(x)
