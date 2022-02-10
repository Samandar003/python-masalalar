# 2-masala
#print("Hello, Python")

# 3-masala
#a=int(input("a = "))
#b=int(input("b = "))
#c=int(input("c = "))
#find_max = max(a, b, c)
#print(f"Eng kattasi: {find_max}")

# 4-masala
#n=int(input("n = "))
#m=n*(n+1)*(n+2)
#print(m%6)

# 5-masala
#a=int(input("a = "))
#b=int(input("b = "))
#son = 0
#if a<b:
#  for i in range(a, b+1):
#    if i%4==0: son += 1
#  print(son)

# 6-masala
#n=int(input("n = "))
#nol=0
#while n%10==0:
#  n=n//10
#  nol+=1
#print(nol)

# hamma nolni sanaydi
#n=int(input("n = "))
#l=0
#for i in range(len(str(n))):
#  if str(n)[i]=="0":
#    l += 1
#print(l)


# 7-masala
#import math
#from math import sqrt
#n=int(input("n = "))
#a=1
#sum = 0
#while a<=n:
#  m=math.sqrt(a)
#  a += 1
#  sum += m
#print(sum)

# 2-usul
#sum = 0
#n=int(input("n = "))
#for i in range(1, n+1):
#  sum = i**(0.5)
#print(sum)

# 8-masala
#n=int(input("n = "))
#l=0
#for i in range(1, n+1):
#  if i%12==0 or i%5==0:
#    #print(i)
#    l+=1
#print(l)


# 10-masala
#n=int(input("n = "))
#numbers = []
#for i in range(n):
#  numbers.append(i)
#print(numbers)
#reversed_digits = reversed(numbers)
#print(list(reversed_digits))

# # 10-masala
# lists = list(map(int, input("Son: ").split()))
# print(*lists[::-1])
# print(lists[::-1])
# #print(lists[::-2])


# 9-masala
#n=int(input("n = "))
#m=int(input("m = "))
#difference = n/m
#print(difference*n)




# for i in range(1, 5):
#   print((1)*i*('*'))

n=int(input("n = "))
nol = 0
while n%10==0:
  n=n//10
  nol += 1
print(nol)

