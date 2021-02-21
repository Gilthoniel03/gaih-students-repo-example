import time
print("WELCOME!")
time.sleep(2)
ingredients = ["Cucumber", "Green pepper", "Cherry tomato", "Lettuce", "Red onion","Corn"]

print("""*************

RECIPE LIST
INGREDIENTS
TIME TO PREPARE

*************  
                    """)

class Recipe:

    def __init__(self, wash, chop, salt ):
        self.wash = wash
        self.chop = chop
        self.salt = salt

class Salad(Recipe):

    time.sleep(2)
    print("Ingredients for salad:", *ingredients, sep = "\n")
    print("----------")

class ChickenSalad(Recipe):

    def __init__(self, wash, chop, salt, cook_chicken, add_chicken ):
        super().__init__(wash, chop, salt )

        self.cook_chicken=cook_chicken
        self.add_chicken=add_chicken
        ingredients.append("Chicken")
        time.sleep(2)
        print("Ingredients for chicken salad:", *ingredients, sep = "\n")
        print("----------")

class TunaSalad(Recipe):

    def __init__(self, wash, chop, salt, open_tuna, add_tuna ):
        super().__init__(wash, chop, salt)

        self.open_tuna=open_tuna
        self.add_tuna=add_tuna

        del(ingredients[0])
        ingredients.append("Tuna")
        ingredients.append("Mayonnaise")
        time.sleep(2)
        print("Ingredients for tuna salad:", *ingredients, sep = "\n")
        print("----------")

salad= Salad("Ingredients are washing..","Ingredients are chopping..","Salt is adding..")
chickensalad = ChickenSalad("Ingredients are washing..","Ingredients are chopping..","Salt is adding..","Chicken is cooking","Chicken is adding")
tunasalad = TunaSalad("Ingredients are washing..","Ingredients are chopping..","Salt is adding..","Canned tuna is opening..","Canned tuna is adding..")

recipe = Recipe('wash', 'chop', 'salt')
recipes = ["Salad:","Chicked salad:","Tuna salad:"]
time_rec= ["15 min","30 min", "20 min"]

time.sleep(2)
for i,j in zip(recipes,time_rec):
    print(i,j)
time.sleep(2)
print("""
Which one do you prefer?
                    
 1. Salad
 2. Chicken Salad
 3. Tuna Salad 

"""
      )


while True:
    option =(input("Please enter the salad number:"))
    if (option == "1"):
        print(salad.wash)
        time.sleep(2)
        print(salad.chop)
        time.sleep(2)
        print(salad.salt)
        time.sleep(2)
        print("Your salad is ready!")
        break
    elif (option =="2"):
        print(chickensalad.wash)
        time.sleep(2)
        print(chickensalad.chop)
        time.sleep(2)
        print(chickensalad.salt)
        time.sleep(2)
        print(chickensalad.cook_chicken)
        time.sleep(2)
        print(chickensalad.add_chicken)
        time.sleep(2)
        print("Your chicken salad is ready!")
        break
    elif (option == "3"):
        print(tunasalad.wash)
        time.sleep(2)
        print(tunasalad.chop)
        time.sleep(2)
        print(tunasalad.salt)
        time.sleep(2)
        print(tunasalad.open_tuna)
        time.sleep(2)
        print(tunasalad.add_tuna)
        time.sleep(2)
        mayonnaise = input("Do you want to add mayonnaise? yes/no")
        if mayonnaise == "yes" :
                print("mayonnaise is adding..")
                time.sleep(2)
                print("mayonnaise added!")
                time.sleep(1)
                print("Your tuna salad is ready!")
        else:
                print("Your tuna salad is ready!")
        break






