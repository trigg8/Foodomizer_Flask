import random
from flask import Flask, render_template, request


app = Flask(__name__)


# List Constants
recipe_list = []

available_recipes = []

Your_meal = ""

ingredients = {"Bun": 1, "Beef Patty": 1, "Lettuce": 1, "Cheese": 1, "Tomato": 1, "Pizza Crust": 1, "Tomato Sauce": 1, "Pork" : 2, "Basil": 1, "Rice": 1, "Bread": 2}

sorted_ingredients = dict(sorted(ingredients.items()))


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
def check_available_recipes(): 
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


# Flask routes
@app.route("/")
def index():
    sorted_ingredients = dict(sorted(ingredients.items()))
    
    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/ingredient_add", methods=["POST"])
def ingredient_add():
    try:
        name = request.form["ingredients_name"]
        num = int(request.form["ingredients_amount"])
        ingredients[name] = num
    except:
        print("Error")

    sorted_ingredients = dict(sorted(ingredients.items()))
    
    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/ingredient_delete/<key>")
def ingredient_delete(key):
    try:
        ingredients.pop(key)
    except:
        print("Error")

    sorted_ingredients = dict(sorted(ingredients.items()))

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/recipe_details/<recipe>", methods=["GET"])
def recipe_details(recipe):    
    temp_list = list(map(str, recipe_list))
    try:
        if recipe in temp_list:
            index = temp_list.index(recipe)
    
        recipe_name = recipe_list[index]
        if type(recipe_list[index]) == Recipe_1:
            ing1 = recipe_list[index].ing1
            ing2 = ""
            ing3 = ""
            ing4 = ""
            ing5 = ""
            ing6 = ""
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = ""
            ni3 = ""
            ni4 = ""
            ni5 = ""
            ni6 = ""
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""
        
        elif type(recipe_list[index]) == Recipe_2:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = ""
            ing4 = ""
            ing5 = ""
            ing6 = ""
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = ""
            ni4 = ""
            ni5 = ""
            ni6 = ""
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_3:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = ""
            ing5 = ""
            ing6 = ""
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = ""
            ni5 = ""
            ni6 = ""
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_4:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = ""
            ing6 = ""
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = ""
            ni6 = ""
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_5:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = ""
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = ""
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_6:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = recipe_list[index].ing6
            ing7 = ""
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = recipe_list[index].ni6
            ni7 = ""
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_7:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = recipe_list[index].ing6
            ing7 = recipe_list[index].ing7
            ing8 = ""
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = recipe_list[index].ni6
            ni7 = recipe_list[index].ni7
            ni8 = ""
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_8:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = recipe_list[index].ing6
            ing7 = recipe_list[index].ing7
            ing8 = recipe_list[index].ing8
            ing9 = ""
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = recipe_list[index].ni6
            ni7 = recipe_list[index].ni7
            ni8 = recipe_list[index].ni8
            ni9 = ""
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_9:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = recipe_list[index].ing6
            ing7 = recipe_list[index].ing7
            ing8 = recipe_list[index].ing8
            ing9 = recipe_list[index].ing9
            ing10 = ""

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = recipe_list[index].ni6
            ni7 = recipe_list[index].ni7
            ni8 = recipe_list[index].ni8
            ni9 = recipe_list[index].ni9
            ni10 = ""

        elif type(recipe_list[index]) == Recipe_10:
            ing1 = recipe_list[index].ing1
            ing2 = recipe_list[index].ing2
            ing3 = recipe_list[index].ing3
            ing4 = recipe_list[index].ing4
            ing5 = recipe_list[index].ing5
            ing6 = recipe_list[index].ing6
            ing7 = recipe_list[index].ing7
            ing8 = recipe_list[index].ing8
            ing9 = recipe_list[index].ing9
            ing10 = recipe_list[index].ing10

            ni1 = recipe_list[index].ni1
            ni2 = recipe_list[index].ni2
            ni3 = recipe_list[index].ni3
            ni4 = recipe_list[index].ni4
            ni5 = recipe_list[index].ni5
            ni6 = recipe_list[index].ni6
            ni7 = recipe_list[index].ni7
            ni8 = recipe_list[index].ni8
            ni9 = recipe_list[index].ni9
            ni10 = recipe_list[index].ni10

    except:
        print("Error")

    return render_template("recipe_details.html", recipe_name = recipe_name, ing1 = ing1, ing2 = ing2, ing3 = ing3, ing4 = ing4, ing5 = ing5, ing6 = ing6, ing7 = ing7, ing8 = ing8, ing9 = ing9, ing10 = ing10, ni1 = ni1, ni2 = ni2, ni3 = ni3, ni4 = ni4, ni5 = ni5, ni6 = ni6, ni7 = ni7, ni8 = ni8, ni9 = ni9, ni10 = ni10)

@app.route("/recipe_delete/<recipe>")
def recipe_delete(recipe):
    temp_list = list(map(str, recipe_list))
    try:
        if recipe in temp_list:
            index = temp_list.index(recipe)
            recipe_list.pop(index)
    except:
        print("Error")

    sorted_ingredients = dict(sorted(ingredients.items()))

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/recipe_create", methods=['POST', 'GET'])
def recipe_create():
    options = ("Recipe 1 Ingredient","Recipe 2 Ingredients","Recipe 3 Ingredients","Recipe 4 Ingredients","Recipe 5 Ingredients","Recipe 6 Ingredients","Recipe 7 Ingredients","Recipe 8 Ingredients","Recipe 9 Ingredients","Recipe 10 Ingredients")
    selected = None
    recipe_name = None
    ing1_name = None
    ing1_amount = None
    ing2_name = None
    ing2_amount = None
    ing3_name = None
    ing3_amount = None
    ing4_name = None
    ing4_amount = None
    ing5_name = None
    ing5_amount = None
    ing6_name = None
    ing6_amount = None
    ing7_name = None
    ing7_amount = None
    ing8_name = None
    ing8_amount = None
    ing9_name = None
    ing9_amount = None
    ing10_name = None
    ing10_amount = None
    
    try:
        if request.method == "POST":
            selected = request.form.get("selector")
            
            recipe_name = request.form["recipe_name"]
            ing1_name = request.form["ing1_name"]
            ing1_amount = request.form["ing1_amount"]
            ing2_name = request.form["ing2_name"]
            ing2_amount = request.form["ing2_amount"]
            ing3_name = request.form["ing3_name"]
            ing3_amount = request.form["ing3_amount"]
            ing4_name = request.form["ing4_name"]
            ing4_amount = request.form["ing4_amount"]
            ing5_name = request.form["ing5_name"]
            ing5_amount = request.form["ing5_amount"]
            ing6_name = request.form["ing6_name"]
            ing6_amount = request.form["ing6_amount"]
            ing7_name = request.form["ing7_name"]
            ing7_amount = request.form["ing7_amount"]
            ing8_name = request.form["ing8_name"]
            ing8_amount = request.form["ing8_amount"]
            ing9_name = request.form["ing9_name"]
            ing9_amount = request.form["ing9_amount"]
            ing10_name = request.form["ing10_name"]
            ing10_amount = request.form["ing10_amount"]

            if selected == "Recipe 1 Ingredient":
                create_new_Recipe_1(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount))

            elif selected == "Recipe 2 Ingredients":
                create_new_Recipe_2(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount))
            
            elif selected == "Recipe 3 Ingredients":
                create_new_Recipe_3(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount))

            elif selected == "Recipe 4 Ingredients":
                create_new_Recipe_4(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount))

            elif selected == "Recipe 5 Ingredients":
                create_new_Recipe_5(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount))

            elif selected == "Recipe 6 Ingredients":
                create_new_Recipe_6(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount), ing6=ing6_name, ni6=int(ing6_amount))

            elif selected == "Recipe 7 Ingredients":
                create_new_Recipe_7(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount), ing6=ing6_name, ni6=int(ing6_amount), ing7=ing7_name, ni7=int(ing7_amount))

            elif selected == "Recipe 8 Ingredients":
                create_new_Recipe_8(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount), ing6=ing6_name, ni6=int(ing6_amount), ing7=ing7_name, ni7=int(ing7_amount), ing8=ing8_name, ni8=int(ing8_amount))

            elif selected == "Recipe 9 Ingredients":
                create_new_Recipe_9(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount), ing6=ing6_name, ni6=int(ing6_amount), ing7=ing7_name, ni7=int(ing7_amount), ing8=ing8_name, ni8=int(ing8_amount), ing9=ing9_name, ni9=int(ing9_amount))
            
            elif selected == "Recipe 10 Ingredients":
                create_new_Recipe_10(name=recipe_name, ing1=ing1_name, ni1=int(ing1_amount), ing2=ing2_name, ni2=int(ing2_amount), ing3=ing3_name, ni3=int(ing3_amount), ing4=ing4_name, ni4=int(ing4_amount), ing5=ing5_name, ni5=int(ing5_amount), ing6=ing6_name, ni6=int(ing6_amount), ing7=ing7_name, ni7=int(ing7_amount), ing8=ing8_name, ni8=int(ing8_amount), ing9=ing9_name, ni9=int(ing9_amount), ing10=ing10_name, ni10=int(ing10_amount))
            else:
                pass
    except:
        print("Error")

    return render_template("recipe_create.html", options = options, selected= selected, recipe_name = recipe_name, ing1_name=ing1_name, ing1_amount=ing1_amount, ing2_name=ing2_name, ing2_amount=ing2_amount, ing3_name=ing3_name, ing3_amount=ing3_amount, ing4_name=ing4_name, ing4_amount=ing4_amount, ing5_name=ing5_name, ing5_amount=ing5_amount, ing6_name=ing6_name, ing6_amount=ing6_amount, ing7_name=ing7_name, ing7_amount=ing7_amount, ing8_name=ing8_name, ing8_amount=ing8_amount, ing9_name=ing9_name, ing9_amount=ing9_amount, ing10_name=ing10_name, ing10_amount=ing10_amount)

@app.route("/check_available")
def check_available():
    try:
        check_available_recipes()
    except:
        print("Error")

    sorted_ingredients = dict(sorted(ingredients.items()))

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/your_meal")
def your_meal():
    try:
        random_meal()
    except:
        print("Error")
    
    sorted_ingredients = dict(sorted(ingredients.items()))

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/accept_choice_yes", methods=["GET", "POST"])
def accept_choice_yes():
    random_meal_list = []
    random_meal_list.append(Your_meal)
    try:
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
    except:
        print("Error")

    
    sorted_ingredients = dict(sorted(ingredients.items()))
    check_available_recipes()

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

@app.route("/accept_choice_no", methods=["GET", "POST"])
def accept_choice_no():
    try:
        random_meal()
    except:
        print("Error")

    sorted_ingredients = dict(sorted(ingredients.items()))

    return render_template("index.html", sorted_ingredients = sorted_ingredients, recipe_list = recipe_list, available_recipes = available_recipes, Your_meal = Your_meal)

# Start app
if __name__ == "__main__":
    app.run(debug=True)