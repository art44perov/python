import random 

def startgame(NoUndestend = False): 
  if NoUndestend == False: 
    print("CHO CHI!\n--- \nStart game. \nIt is necessary to guess an even or even number will be. Will the number be even? y/n") 
  answer = input("") 
  if answer == "y" or answer == "Y" or answer == "n" or answer == "N": 
    Game(answer) 
    return True 
  print("No andestene. Try again") 
  startgame(True) 

def Game(answer): 
  randNum = random.randint(1,999) 
  #print(randNum) 
  #print(randNum%2) 
  print("Number computer = " + str(randNum)) 
  if randNum%2 == 0 and (answer == "y" or answer == "Y"): 
    print("Winner!!") 
  elif randNum%2 == 1 and (answer == "n" or answer == "N"): 
    print("Winner!!") 
  else: 
    print("Looser!!") 
  return True 
     
startgame()
