def dekorotiv_func(func):
  def ichki(qiymatlar):
    return [func(val[0], val[1], val[2], val[3]) for val in qiymatlar]
  return ichki
@dekorotiv_func
def qoshish(a, b, c, d):
  print(a+b+c+d)
(qoshish([(1, 2, 3, 4), (5, 6, 7, 8)]))

@dekorotiv_func
def ayirish(a, b, c, d):
  print(a-b-c-d)
(ayirish([(8, 7, 6, 5), (4, 3, 2, 2)]))

@dekorotiv_func
def bolish(a, b, c, d):
  print(a//b//c//d)
(bolish([(800, 7, 6, 5), (40, 3, 2, 2)]))

@dekorotiv_func
def kopaytirish(a, b, c, d):
  print(a*b*c*d)
kopaytirish([(1, 2, 3, 4), (5, 6, 7, 8)])

