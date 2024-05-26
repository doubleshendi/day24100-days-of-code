import random
#def whichcake(ingredient, base, coating):
  #if ingredient == "chocolate":
    #print("Mmm, chocolate cake is amazing")
  #elif ingredient == "broccoli":
    #print("You what mate?!")
  #else:
    #print("Yeah, that's great I suppose...")
  #print("So you want a", ingredient, "cake on a", base, #"base with", coating,"")

#useringredient = input("Name an ingredient: ")
#userbase = input("Name a type of base: ")
#usercoat = input("Favourite cake topping: ")


#whichcake(useringredient, userbase, usercoat)
  
print("Infinity Dice 🎲")
print()


sides = int(input("How many sides?: "))

def rollDice(sides):
  print("You rolled", random.randint(1,sides))
  
rollDice(sides)
print()
rollagain = input("Roll again? ")
while (rollagain == "yes" or rollagain == "Yes"):

 rollDice(sides)
 print()
 rollagain = input("Roll again? ")

