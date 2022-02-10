# 1-masal
# lists = list(map(int, input("...").split()))
# for x in lists:
#   if x%2==0:
#     print(x)

# 2-masala
# numbers = list(map(int, input("... ").split()))
# for x in numbers:
#   if x%2!=0:
#     print(x)

# 3-masala
# numbers = list(map(int, input("... ").split()))
# if len(numbers)>2:
#   print(numbers[-2:])
# else: print(False)

# # 4-masala
# numbers = list(map(int, input("... ").split()))
# while numbers:
#   if numbers[0]:
#     print(numbers[0])
#     del numbers[0]
#   print(numbers.pop())
# 2-usul

numbers = list(map(int, input(".... ").split()))
if len(numbers)%2==0:
  for x in range(len(numbers)//2):
    print(numbers[x])
    print(numbers[len(numbers)-1-x])
else: 
  for y in range(len(numbers)//2):
    print(numbers[y])
    print(numbers[len(numbers)-1-y])
  print(numbers[len(numbers)//2])

# 5-masala
# numbers = list(map(int, input("... ").split()))
# maximum = max(numbers)
# if maximum%2==0:
#   print(maximum)
# else: print(numbers[0])

# 6-masala
# numbers = list(map(int, input("... ").split()))
# manfiy = 0
# for x in numbers:
#   if x<0:
#     manfiy+=x
# print(manfiy)

# 7-masala
# numbers = list(map(int, input("... ").split()))
# nums = []
# for x in numbers:
#   n = numbers.count(x)  
#   if n==2: print(x)

# 8-masala
# nums = []
# numbers = list(map(int, input("... ").split()))
# for x in numbers:
#   n = (abs(x))
#   nums.append(n)
# print(min(nums))

# 9-masala
# numbers = list(map(int, input("... ").split()))
# for x in numbers:
#   if x==0:
#     continue
#   else:
#     print(x, end=" ")

# 10-masala
# numbers = list(map(int, input("... ").split()))
# nums = []
# for x in numbers:
#   count = numbers.count(x)
#   if count==3:
#     print(x) 

# 11-masala
# numbers = list(map(int, input("... ").split()))
# nums = 1
# for x in numbers:
#   count = numbers.count(x)
#   if count==1:
#     nums*=x
# print(nums)

# 12-masala
# numbers = list(map(int, input("... ").split()))
# count = 0
# n = 0
# for x in numbers:
#   count+=1
#   n+=x
# m = n//count
# print(n//count)  
# while True:
#   numbers = list(map(int, input("... ").split()))  
#   for x in numbers:
#     if x>m:
#       count+=1
#       n+=x
#       if count==5: 
#         break
#   print(n//count)
    
# 13-masala
# numbers = list(map(int, input("... ").split()))
# max = max(numbers)
# print(max)
# print(max+1)

# 14-masala
# numbers = list(map(int, input("... ").split()))
# for x in numbers:
#   for j in range(1, x+1):
#     if j**3==x:
#       print(x, end=', ')

