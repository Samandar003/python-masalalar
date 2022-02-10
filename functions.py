# 8. Barcha 3 xonali sonlar ichida raqamlari ko'paytmasi raqamlari yig'indisiga bo'linadiganlarini chiqaring.(20ball)
# for i in range(100, 1000):
#   n = i%10
#   m = i//10%10
#   l = i//100
#   kopaytma = n*m*l
#   summa = n+m+l
#   if kopaytma%summa==0:
#     print(i)
n = 0
m = 1
for i in range(11):
  i += 1
  n += i
  m *= n
  print(f"Yigindisi: {n}")
  print(f"Kopaytmasi: {m}")


