import os, time

health = 100
sword = False
left1 = False
key = False 
mimic1 = False
mimic2 = False
gift = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome explorers! You are the character John Cena exploring through catacombs.")
  print()
  print()
  print("Let's get started!")
  time.sleep(3) # wait 3 seconds before moving on
  room1() # runs to send the player to cave #1

def room1():
  global sword, left1, health # use the shovel variable from the top
  os.system('clear')
 
  if left1==True:
    print("You have confronted the skeleton but you have no weapon...")
    time.sleep(4)
    print("You are forced to fight the skeleton, after serveral swings punching him, he crumbles falling to the ground.")
    health = 75
    time.sleep(5)
    print("You lost 25 HP in the fight there is only one more way to go so you travel right to the next room")
    time.sleep(6)
    room2()
  
  elif sword:
    print("The pile of bones starts to shake and turns into a skeleton. Would you like to fight it, go left, or go right")
  
  else:
    print("You are in the beginning of the catacombs. There is a sword on the ground next to a pile of bones, a room to your left, and a tunnel to your right. What would you like to do?")
  decision = input(">>").strip().lower()
  
  if decision.find("sword") > -1:
    print("You have picked up the sword...")
    sword = True
    time.sleep(3)
    room1()
  
  elif decision.find("left") > -1 and sword==True:
    print("You tried to walk into the room on the left but the door is shut, you are forced to confront the skeleton.")#finish this segment
    time.sleep(3)
    print("You hit the skeleton once with you're sword and it crumbled to the ground turning back into a pile of bones...")
    time.sleep(3)
    print("Your only choice now is to continue to the right")
    room2()
  
  elif decision.find("left") > -1 and sword==False:
    print("You tried to walk into the room on the left but the door shut and you are unable to continue this way.")
    time.sleep(3)
    left1 = True
    print("You turn back and there is a skeleton with a sword standing over you")
    time.sleep(5)
    room1()
 
  elif decision.find("right") > -1:
    print("You walk through the entrance on the right and the door shuts immediately after you pass through it, on the side you came from there is an angry skeleton trying to attack you")
    time.sleep(7)
    room2()
 
  elif decision.find("fight") > -1:
    print("You have chosen to fight the skeleton with your sword...")
    time.sleep(4)
    print("He swings at you but luckily he misses and you counter with your sword and he crumbles falling to the ground")
    time.sleep(6)
    print("There are two ways for you to go but you notice that while fighting the skeleton the door on your left closed so you are forced to go on the room to the right.")
    time.sleep(6)
    room2()
  
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    room1()
  

def room2():
  global key, health, mimic1, mimic2
  os.system('clear')
  print("Welcome to room 2")

  if health <= 0:
    death()
  
  elif key == True:
    print("It looks like you can use that key to open up the door and continue to the next room.")
    time.sleep(4)
    room3()
    
  elif key == True and health == 5:
    print("It looks like you can use that key to open up the door and continue to the next room...")
    time.sleep(4)
    print("As you're walking through the doorway the door shuts down on you killing you")
    time.sleep(3)
    death()

  elif mimic1 == True and mimic2 == False:
    print("After your fight against the mimic you can now choose to open chest 2 or 3 or go through the door")

  elif mimic1 == False and mimic2 == True:
    print("After your fight against the mimic you can now choose to open chest 1 or 2 or go through the door")

  elif mimic1 == True and mimic2 == False:
    print("It looks like your only options now are to open chest 2 or go through the door")
  
  elif key== False and mimic1 == False and mimic2 == False:
    print("You are now in the second room of the catacombs and you see three treasure chests and a door. You can try to go through the door, open chest 1, 2, or 3 ")
  decision = input(">>").strip().lower()
  
  if decision.find("door") > -1 and key == False:
    print("You try to open the door but it apears to be locked and it wont budge...")
    time.sleep(4)
    print("You're going to have to find a key somehow")
    time.sleep(4)
    room2()
  
  elif decision.find("1") > -1 and sword == True:
    print("You walk up to the first chest and open it, but the chest ends up becoming a mimic and attaks you...")
    time.sleep(5)
    print("Luckily you were prepared and had your newly found sword on you, so you strike the mimic several time and it dies. Sadly you lost 10 HP in the fight")
    health = health-10
    time.sleep(5)
    mimic1 = True
    room2()

  elif decision.find("1") > -1 and sword == False:
    print("You walk up to the first chest and open it, but the chest ends up becoming a mimic and attaks you... ")
    time.sleep(5)
    print("You have to resort to fighting the beast with your bare hands...")
    time.sleep(4)
    print("After a strugling fight you beat the monster but in the proccess you lose 70 HP")
    health = health-70
    mimic1 = True
    time.sleep(4)
    room2()

  elif decision.find("2") > -1:
    print("You walk up to the second chest and open it, inside you find a key...")
    print("I wonder what that could be used for???")
    time.sleep(4)
    key=True
    room2()

  elif decision.find("3") > -1 and sword == True:
    print("You walk up to the first chest and open it, but the chest ends up becoming a mimic and attaks you...")
    time.sleep(5)
    print("Luckily you were prepared and had your newly found sword on you, so you strike the mimic several time and it dies. Sadly you lost 10 HP in the fight")
    health = health-10
    time.sleep(5)
    mimic2 = True
    room2()

  elif decision.find("3") > -1 and sword == False:
    print("You walk up to the first chest and open it, but the chest ends up becoming a mimic and attaks you... ")
    time.sleep(5)
    print("You have to resort to fighting the beast with your bare hands...")
    time.sleep(4)
    print("After a struggling fight you beat the monster but in the proccess you lose 70 HP")
    health = health-70
    mimic2 = True
    time.sleep(4)
    room2()

  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    room2()

def room3():
  global sword, health, gift
  os.system('clear')
  
  if gift == False:
    print("You have entered the last room of the catacombs. There is an open door at the end of the room and a pedistool with some type of treasure in the center of the room. Choose what you would like to do")
    decision = input(">>").strip().lower()

  elif decision.find("door") > -1:
    print()
    time.sleep(4)
    endGame()

  elif decision.find("pedistool") > -1:
    print("After you pick up the treasure you start to hear strange mechanical sounds...")
    time.sleep(4)
    print("after a few seconds a rock falls from the ceiling and crushes you to death")
    time.sleep(4)
    death()

  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    room3()

def endGame():
  os.system("clear")
  pass

def death():
  os.system("clear")
  print("You Died")
  pass

startGame()