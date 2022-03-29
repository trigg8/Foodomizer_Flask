import random
import json
import pickle
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# List Constants
recipe_list = []

available_recipes = []

sorted_available_recipes = list(sorted(available_recipes))

Your_meal = ""

ingredients = {"Bun": 1, "Beef Patty": 1, "Lettuce": 1, "Cheese": 1, "Tomato": 1, "Pizza Crust": 1, "Tomato Sauce": 1, "Pork" : 2, "Basil": 1, "Rice": 1, "Bread": 2}

sorted_ingredients = dict(sorted(ingredients.items()))

#ingredients = {}


# Recipe Classes
class Recipe_1:
    def __init__(self,name,ing1,ni1):
        self.name = name
        self.ing1 = ing1 
        self.ni1 = ni1
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_2:
    def __init__(self,name,ing1,ni1,ing2,ni2):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ni1 = ni1
        self.ni2 = ni2
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_3:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_4:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_5:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)        
class Recipe_6:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ing6 = ing6
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.ni6 = ni6
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_7:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ing6 = ing6
        self.ing7 = ing7
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.ni6 = ni6
        self.ni7 = ni7
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_8:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ing6 = ing6
        self.ing7 = ing7
        self.ing8 = ing8
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.ni6 = ni6
        self.ni7 = ni7
        self.ni8 = ni8 
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_9:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ing6 = ing6
        self.ing7 = ing7
        self.ing8 = ing8 
        self.ing9 = ing9
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.ni6 = ni6
        self.ni7 = ni7
        self.ni8 = ni8
        self.ni9 = ni9
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)
class Recipe_10:
    def __init__(self,name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9,ing10,ni10):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4
        self.ing5 = ing5
        self.ing6 = ing6
        self.ing7 = ing7
        self.ing8 = ing8 
        self.ing9 = ing9
        self.ing10 = ing10
        self.ni1 = ni1
        self.ni2 = ni2
        self.ni3 = ni3
        self.ni4 = ni4
        self.ni5 = ni5
        self.ni6 = ni6
        self.ni7 = ni7
        self.ni8 = ni8
        self.ni9 = ni9
        self.ni10 = ni10
        self.add_to_recipe_list()    
    def __repr__(self):
        return self.name
    def add_to_recipe_list(self):
        if self not in recipe_list:
            recipe_list.append(self)


# Test Recipes
Recipe_5("Hamburger", "Bun", 1, "Beef Patty",1, "Lettuce",1, "Cheese",1, "Tomato", 1)

Recipe_3("Pizza", "Pizza Crust",1, "Tomato Sauce",1, "Cheese",1)

Recipe_3("GaPoa Mu","Pork",1, "Basil",1, "Rice",1)

Recipe_1("Grilled Pork", "Pork", 2)


# Create New Recipes for all Classes
def create_new_Recipe_1(name, ing1, ni1):
    Recipe_1(name, ing1, ni1)
def create_new_Recipe_2(name,ing1,ni1,ing2,ni2):
    Recipe_2(name,ing1,ni1,ing2,ni2)
def create_new_Recipe_3(name,ing1,ni1,ing2,ni2,ing3,ni3):
    Recipe_3(name,ing1,ni1,ing2,ni2,ing3,ni3)
def create_new_Recipe_4(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4):
    Recipe_4(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4)
def create_new_Recipe_5(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5):
    Recipe_5(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5)
def create_new_Recipe_6(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6):
    Recipe_6(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6)
def create_new_Recipe_7(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7):
    Recipe_7(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7)
def create_new_Recipe_8(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8):
    Recipe_8(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8)
def create_new_Recipe_9(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9):
    Recipe_9(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9)
def create_new_Recipe_10(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9,ing10,ni10):
    Recipe_10(name,ing1,ni1,ing2,ni2,ing3,ni3,ing4,ni4,ing5,ni5,ing6,ni6,ing7,ni7,ing8,ni8,ing9,ni9,ing10,ni10)



# Functions
def check_avialable_recipes(): 
    global available_recipes
    available_recipes = []
    for rcp in recipe_list: 
        try:
            if type(rcp) == Recipe_1:
                if ingredients[rcp.ing1] >= rcp.ni1:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_2:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_3:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_4:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_5:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5: 
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_6:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5 and ingredients[rcp.ing6] >= rcp.ni6: 
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_7:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5 and ingredients[rcp.ing6] >= rcp.ni6 and ingredients[rcp.ing7] >= rcp.ni7:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_8:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5 and ingredients[rcp.ing6] >= rcp.ni6 and ingredients[rcp.ing7] >= rcp.ni7 and ingredients[rcp.ing8] >= rcp.ni8:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_9:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5 and ingredients[rcp.ing6] >= rcp.ni6 and ingredients[rcp.ing7] >= rcp.ni7 and ingredients[rcp.ing8] >= rcp.ni8 and ingredients[rcp.ing9] >= rcp.ni9:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
            elif type(rcp) == Recipe_10:
                if ingredients[rcp.ing1] >= rcp.ni1 and ingredients[rcp.ing2] >= rcp.ni2 and ingredients[rcp.ing3] >= rcp.ni3 and ingredients[rcp.ing4] >= rcp.ni4 and ingredients[rcp.ing5] >= rcp.ni5 and ingredients[rcp.ing6] >= rcp.ni6 and ingredients[rcp.ing7] >= rcp.ni7 and ingredients[rcp.ing8] >= rcp.ni8 and ingredients[rcp.ing9] >= rcp.ni9 and ingredients[rcp.ing10] >= rcp.ni10:
                    if rcp.name not in available_recipes:
                        available_recipes.append(rcp)
        except KeyError:
            continue


def random_meal():
    global Your_meal
    Your_meal = random.choice(available_recipes)
    return Your_meal

def accept_choice():
    random_meal_list = []
    #print(random_meal_list)
    random_meal()
    random_meal_list.append(Your_meal)
    #print(random_meal_list)
    print("Your Meal is: ", Your_meal)
    accept = input("Do you accept this choice? Yes or No: ")
    if accept == "Yes":
        for rcp in random_meal_list:
            if type(rcp) == Recipe_1:
                ingredients[rcp.ing1] -= rcp.ni1
            elif type(rcp) == Recipe_2:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
            elif type(rcp) == Recipe_3:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
            elif type(rcp) == Recipe_4:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
            elif type(rcp) == Recipe_5:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
            elif type(rcp) == Recipe_6:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
            elif type(rcp) == Recipe_7:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
            elif type(rcp) == Recipe_8:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
            elif type(rcp) == Recipe_9:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
                ingredients[rcp.ing9] -= rcp.ni9
            elif type(rcp) == Recipe_10:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
                ingredients[rcp.ing9] -= rcp.ni9
                ingredients[rcp.ing10] -= rcp.ni10
    
    elif accept == "No":
        accept_choice()

    else: 
        accept_choice_alt()
        
def accept_choice_alt():
    random_meal_list = [Your_meal]
    accept = input("Please Type Yes or No: ")
    if accept == "Yes":
        for rcp in random_meal_list:
            if type(rcp) == Recipe_1:
                ingredients[rcp.ing1] -= rcp.ni1
            elif type(rcp) == Recipe_2:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
            elif type(rcp) == Recipe_3:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
            elif type(rcp) == Recipe_4:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
            elif type(rcp) == Recipe_5:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
            elif type(rcp) == Recipe_6:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
            elif type(rcp) == Recipe_7:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
            elif type(rcp) == Recipe_8:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
            elif type(rcp) == Recipe_9:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
                ingredients[rcp.ing9] -= rcp.ni9
            elif type(rcp) == Recipe_10:
                ingredients[rcp.ing1] -= rcp.ni1
                ingredients[rcp.ing2] -= rcp.ni2
                ingredients[rcp.ing3] -= rcp.ni3
                ingredients[rcp.ing4] -= rcp.ni4
                ingredients[rcp.ing5] -= rcp.ni5
                ingredients[rcp.ing6] -= rcp.ni6
                ingredients[rcp.ing7] -= rcp.ni7
                ingredients[rcp.ing8] -= rcp.ni8
                ingredients[rcp.ing9] -= rcp.ni9
                ingredients[rcp.ing10] -= rcp.ni10
    
    elif accept == "No":
        accept_choice()

    else: 
        accept_choice_alt()


# Ingredient Funtions
def add_ingredient(name):
    ingredients[name] += 1

def remove_ingredient(name):
    ingredients[name] -= 1

def add_mult_ingredients(name, num):
    ingredients[name] += num

def remove_mult_ingredients(name, num):
    ingredients[name] -= num

def add_new_ingredient(name):
    ingredients[name] = 1

def add_mult_new_ingredients(name, num):
    ingredients[name] = num

def print_ingredients():
    print("Ingredients in list are: ", ingredients)



# Flask routes
@app.route("/")
def index():
    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, sorted_available_recipes = sorted_available_recipes, Your_meal = Your_meal)

@app.route("/ingredient_add", methods=["POST"])
def ingredient_add():
    name = request.form["ingredients_name"]
    num = request.form["ingredients_amount"]
    ingredients[name] = num
    sorted_ingredients = dict(sorted(ingredients.items()))
    print(ingredients)
    print(sorted_ingredients)
    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, sorted_available_recipes = sorted_available_recipes, Your_meal = Your_meal)

# Start app
if __name__ == "__main__":
    app.run(debug=True)