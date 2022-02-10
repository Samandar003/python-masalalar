# numbers = [23, 2, 0, 87, 5, 0]

# def sort_list(numbers):
#   for x in range(len(numbers)):
#     min_value = min(numbers[x:])
#     min_index = numbers.index(min_value)
#     numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
# numbers = [34, 2, 3, 9, 5]
# sort_list(numbers)
# print(numbers)

# for x in range(len(numbers)-1):
#   min_value = min(numbers[x:])
#   min_index = numbers.index(min_value, x)
#   # print(min_index)
#   numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
#   print(numbers)

# print(numbers)
# for x in range(len(numbers)-1):
#   min_val = min(numbers[x:])
#   min_index = numbers.index(min_val, x)
#   if numbers[x] != numbers[min_index]:
#     numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
# print(numbers)

# for x in range(len(numbers)-1):
#   m_val = numbers[x]
#   for j in range(x+1, len(numbers)):
#     if numbers[j] < m_val:
#       m_val = numbers[j]
#   m_index = numbers.index(m_val, x)
#   if numbers[x] != numbers[m_index]:
#     numbers[x], numbers[m_index] = numbers[m_index], numbers[x]
# print(numbers)

# index() descending
num = int(input("How many numbers you want to enter: "))
numbers = [int(input(f"Enter {x+1}-number: ")) for x in range(num)]
for x in range(len(numbers)-1):
  min_index = x
  for j in range(x+1, len(numbers)):
    if numbers[j] > numbers[min_index]:
      min_index = j
  if numbers[x] != numbers[min_index]:
    numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
print(numbers)



