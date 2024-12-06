import random

def main():
  i = 0 
  password = ""
  
  lenpass = input("Enter the password length:")

  if lenpass.isnumeric() == False:
    print("Error")
    return
  else:
    lenpass = int(lenpass)

  while i < lenpass:
    password = password + GeneratorSymbol()
    i = i + 1

  print("Password: " + str(password))

def GeneratorSymbol():
  library = "qazwsxedcrfvtgbyhnujmik,ol.p;/[\0123456789*-+!@#$?%&()~=QWERTYUIOPLKJHGFDSAZXCVBNM<>|_`" 
  array = list(library)
  return array[random.randint(0, len(library))]

main()
