# #if,else:
# #2-m
# # n =int(input())
# # if n % 2 ==0:
# #     print("juft")
# # else:
# #     print("toq")


# #6-m
# # n = int(input())
# # a = n % 100
# # if a % 3 == 0:
# #     print("bo'linadi")

# # else:
# #     print(False)


# #8.
# n = int(input())
# if len(str(n)) !=6:
#     print(False)
# else:
#     oxirgi  = n % 10 
#     oxirgi_2  = n %100//10
#     oxirgi_3 = n % 1000//100
#     boshi_3 = n % 10000//1000
#     boshi_2 = n % 100000//10000
#     boshi = n //100000
#     if oxirgi+oxirgi_2+oxirgi_3 == boshi+boshi_2+boshi_3:
#         print(True)
#     else:
#         print(False)



# #1-m.Musobaqa
# a = int(input())
# b = int(input())
# print(a-(-b))

# #4
# n =int(input())
# c = n*(n+1)*(n+2) 
# a =c % 6
# print(a)
# print(0)

#5
# a = int(input())
# b = int(input())
# son = 0

# if a<b:
#     for i in range(a,b+1):
#         if i % 4 == 0:
#             son+=1
#     print(son)





# l_nol = 0

# while n % 10 ==0:
#     l_nol+=1
#     n = n //10
    
# print(l_nol)

#7-m
# n =int(input())
# sum = 0
# for i in range(1,n+1):
#     sum+=i**(1/2)

# print(sum)


#8-m
# n = int(input())

# l = 0

# for i in range(1,n+1):
#     if i % 12 == 0  or i % 5 ==0:
#         print(i)
#         l+=1
# print(l)

#9-m

# n = int(input())
# m = int(input())
# c = n / m
# print(n * c)


# 1 2 3 4 5 6
# 6 5 4 3 2 1

#10-m

lists = list(map(int,input("sonlar kiriting probel bolsin orasida:  ").split()))
print(*lists[::-1])














