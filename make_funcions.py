# x, y = map(int, input('... ').split())

# append
# extend
# index
# remove
# pop
# sort
# reverse
#count
#insert

# 1-misol,   append()
# num = []
# def number(a):
#   num.extend(a)
#   return num
# print(number([2, 5, 6, 8]))

# # 2-usul
# num = []
# def number(a):
#   num=[a]
#   return num
# print(number(5))

# 2-misol,  extend()
# def number(num1, num2):
#   sum = num1+num2
#   return sum
# print(number([1, 2, 3, 4], [5, 6, 7]))

# 3-misol,   index()
# numbers = [1, 2, 3, 4, 5, 6]
# def index(num):
#   nol = 0
#   for x in numbers:
#     if x==num:
#       return nol
#     else: 
#       nol+=1
#       x+=1
# print(index(6))

# 4-misol,  remove()
# text = 'men python dasturchiman'
# print(text)
# def remove_str(satr):
#   #if text.find(satr)
#   return text.replace(satr, '')
# print(remove_str('python'))

# 2-usul
# fruits = ['apple', 'penny', 'banana', 'potato']
# def remove(thing):
#   num = fruits.index(thing)
#   del fruits[num]
#   return fruits
# print(remove('apple'))

# 5-misol,   pop()
# fruits = ['apple', 'penny', 'banana', 'potato']
# def remove(thing):
#    fruits.remove(thing)
#    return fruits
# print(remove('apple'))

# 6-misol,  sort()
# def sort_list(numbers):
#   for x in range(len(numbers)):
#     min_value = min(numbers[x:])
#     min_index = numbers.index(min_value)
#     numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
# numbers = [34, 2, 3, 9, 5]
# sort_list(numbers)
# print(numbers)


# 7-misol,    reverse()
# def reverse_list(number):
#   return number[::-1]
# print(reverse_list([4, 54, 9, 3, 5]))

# 8-misol,  count()
# numbers = [2, 3, 4, 2, 8, 2, 23, 2]
# def count_num(num):
#   sana = 0
#   for x in numbers:
#     if x==num:
#       sana+=1
#   return sana
# print(count_num(2))

# 9-misol,  insert()
# numbers = ['a', 'b', 'c', 'd', 'e']
# def inser_list(index, thing):
#   del numbers[index]
#   numbers.append(thing)
# print(inser_list(2, 's'))
# print(numbers)

