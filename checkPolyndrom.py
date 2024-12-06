#Проверка на введеной строки на палиндром

def Main():
  my_str = input("Введите строку для проверки...")
  if ControlNumber(my_str) == False:
    print("Строка введена с ошибкой! Попробуйте снова...")
    Main()
  my_str = my_str.casefold()
  rev_str = reversed(my_str)
  if list(my_str) == list(rev_str):
    print("Введеная строка является палиндромом")
  else:
    print("Введеная строка не является палиндромом")

def ControlNumber(my_str):
  for number in range(0,10):
   ConNum = my_str.find(str(number))
   if str(ConNum) != "-1":
    return False

  return True
  
    
Main()
