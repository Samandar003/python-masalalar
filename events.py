import threading as thng
event = thng.Event()

def jarayon():
  print("Mahinani o't oldirish. ")
  event.wait()
  print("Mahinani o't oldirish boshlandi.")
t1 = thng.Thread(target=jarayon)
t1.start()

question = input("Mahinani o't oldirish boshlansinmi? (yes\ no): ")
if question=='yes':
  event.set()
  