# 1-misol
# class Mashinalar:
#   def __init__(self, kompaniya, model, rangi):
#     self.kompaniya = kompaniya
#     self.model = model
#     self.rangi = rangi

#   def __str__(self):
#     return "Ishlab chiqaruvchi: {}, \nModeli: {}, \nRangi: {}\n".format(self.kompaniya, self.model, self.rangi)

# class Gm(Mashinalar):
#   def __init__(self, kompaniya, model, rangi, narxi):
#       super().__init__(kompaniya, model, rangi)
#       self.narxi = narxi
#   def __str__(self):
#       text = super(Gm, self).__str__()
#       text += "Narxi: {}".format(self.narxi)
#       return text
# mashina1 = Gm('Tesla', 'Tesla_S', 'qora', 2000)
# print(mashina1)


# 2-misol
# class Restaurant:
#   def __init__(self, nomi, lokatsiyasi, sifati):
#       self.nomi = nomi
#       self.lokatsiyasi = lokatsiyasi
#       self.sifati = sifati
#   def __str__(self) -> str:
#     return "Reatarant nomi: {}\nJoylashgan joyi: {}\nSifati: {}".format(self.nomi, self.lokatsiyasi, self.sifati)
  
# class Tanho_restaran(Restaurant):
#   def __init__(self, nomi, lokatsiyasi, sifati, taom_soni):
#       super().__init__(nomi, lokatsiyasi, sifati)
#       self.taom_soni = taom_soni
#   def __str__(self) -> str:
#       extra_info = super(Tanho_restaran, self).__str__()
#       extra_info += "Taomlar soni: {}".format(self.taom_soni)
#       return extra_info
# restaran1 = Tanho_restaran('Joziba', 'shahar-markazida', 'yaxshi', 15)
# print(restaran1)

# 3-misol
class University:
  def __init__(self, name, faculty, reyting):
    self.name = name
    self.faculty = faculty
    self.reyting = reyting

  def __str__(self) -> str:
    return "Universitet nomi: {}\nFaculteti: {}\nReytingi: {}\n".format(self.name, self.faculty, self.reyting)

class Harvard(University):
  def __init__(self, name, faculty, reyting, number_students):
      super().__init__(name, faculty, reyting)
      self.number_students = number_students
  def __str__(self) -> str:
      text = super(Harvard, self).__str__()
      text += "Studentlari soni: {}".format(self.number_students)
      return text
universitet1 = Harvard('MIT', 'Technology', 2, 350000)
print(universitet1)

