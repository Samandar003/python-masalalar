#  1 - masala
# n = int(input("n = "))
# s = input("Satrni kiriting: ")
# if n==len(s):
#   print(True)
# else: print(False)

# 2-masala
# n = int(input("n = "))
# m = int(input("m = "))
# print(int(n/m))

# 3-masala
# n = int(input("n = "))
# sum = 1
# for x in range(1, n+1):
#   sum *= x
#   x += 1
# print(sum)

# 4-masala
# s = input("Satrni kiriting: ")
# print(s)
# print(len(s))
# print(len(s[1:-1]))
# print(s[1:-1])

# 5-masala
# s = input("Satrni kiriting: ").lower()
# length = len(s[1:-1])
# if length%2==0:
#   print(True)
# else: print(False)

# 6-masala
# s = input("Satrni kiriting: ")
# if s.isdigit():
#     print(True)
# else: print(False)

# 6-masala
# s = input("Satrni kiriting: ")
# if s.isalpha():
#     print(True)
# else: print(False)

# 7-masala
numbers = list(map(int, input("... ").split()))  
sum = 0
for x in numbers:
  sum+=x
  
if 9<sum<100:
  print(True)
else: print(False)

