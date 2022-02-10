import time as tm
def svetofor():
  print('qizil chiroq')
  print('haydovchi 30 sekund kuting')
  for i in range(30,0,-1):
    tm.sleep(1)
    print(i)
  print('sariq chiroq')
  print("Biroz kutamiz")
  tm.sleep(5)
  print('yashil chiroq')
  print('start')

svetofor()
