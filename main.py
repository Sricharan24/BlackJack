import random
import time

cardNames = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}


def printHand(hand):
  outputHand = []
  for num in hand:
    if num == 1 or num > 10:
      outputHand.append(cardNames[num])
    else:
      outputHand.append(num)
  print(outputHand)
  print()


def calcHandValues(hand):
  sum1 = 0
  numAces = 0
  for num in hand:
    if num == 1:
      numAces += 1
      sum1 += 1
    elif num > 10:
      sum1 += 10
    else:
      sum1 += num
  values = [sum1]
  for i in range(1,numAces+1):
    values.append(sum1 + i * 10)
  return values


def getFinalValue(hand):
  finalValue = 0
  values = sorted(calcHandValues(hand))
  for num in values:
    if num <= 21:
      finalValue = num
  return finalValue

while True:
  playerHand = []

  for i in range(2):
   playerHand.append(random.randint(1,13))
  
  print("Here is your hand: ")
  printHand(playerHand)

  if getFinalValue(playerHand) == 21:
    print("You win")
  x=True
  while x:
    enter = input("Type in H to hit or S to stay:")
    if enter == "h":
      playerHand.append(random.randint(1,13))
      print("Here is your hand: ")
      printHand(playerHand)
      handValues = calcHandValues(playerHand)
      if min(handValues) > 21:
        print("You lost")
        break
      elif getFinalValue(playerHand) == 21:
        print("You win")
        break
    
    if enter == "s":
      print("Dealer's turn!\n")
      dealerHand = []
      for i in range(2):
        dealerHand.append(random.randint(1,13))
      print("Here is the dealer's hand: ")
      printHand(dealerHand)
      while True:
        x = False
        time.sleep(3) 
        handValues = calcHandValues(dealerHand)
        if min(handValues) < 17:
          dealerHand.append(random.randint(1,13))
          print("dealer's new hand:")
          printHand(dealerHand)
        elif handValues == 21:
          print("The dealer won!")
          break
        elif min(handValues) > 21:
          print("You win")
          break
        else:
          if getFinalValue(playerHand) > getFinalValue(dealerHand):
            print("You win\n")
          else:
            print("The dealer won\n")
          break
  input("Press Enter to play again!\n")

