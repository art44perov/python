import random

life = 5
bank = 0

#print(random_number)
def Main():
  global life
  life = 5
  random_number = random.randint(0, 100)
  print(
        "Я загадал число от 0 до 100. Готов дать 100$ если угадаешь его! Даю " + str(life) + " попыток."
  )
  #print(random_number)
  Game(random_number)
      
def ControlCorrectEnter(x):
    try:
        int(x)
        return True
    except:
        return False

def Game(u_num):
  global bank
  global life
  MassageUser()
  if life == 0:
    print("Сожалею, но у вас закончились попытки, вы проиграли")
    Fall() 
    return 
    
  print("Введи число... (осталось " + str(life) + " попыток)")
  x = input("")
      
  if not ControlCorrectEnter(x):
    print("Не включай дурака и введи число нормально...")
    Game(u_num)

  x = int(x)

  if x > u_num:
    life = life - 1
    print("Не угадал, мое число меньше")
    Game(u_num)
  elif x == u_num:
    bank = bank + 100
    Win()
  else:
    life = life - 1
    print("Не угадал, мое число больше")
    Game(u_num)

def Win():
  print("Молодей! Ты угадал! Твой банк = " + str(bank))
  Question()

def Fall():
  print("Ты проиграл")
  Question()

def Question():
  global bank

  print("Хочешь играть еще? (Y - да / N - нет)")
  x = input("")
  if x == "y" or x == "Y":
    print("Сохранить банк или все сначала? (Y - да, сохранить / N - нет)")
    b = input("")
    if b == "n" or b=="N":
      bank = 0

    Main()
  else: return

def MassageUser():
  global bank
  global life
  print("")
  print("----------------")
  print("Жизни : " + str(life))
  print("Банк : " + str(bank))
  print("----------------")
  print("")
  
Main()
