spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods = spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return(food_names)
    #pass
#get_names()

def get_spiciest_foods(spicy_foods = spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return(spiciest_foods)
    #pass
#get_spiciest_foods()

def print_spicy_foods(spicy_foods = spicy_foods):
    for food in spicy_foods:
        spicy_food_printer = (f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
        print(spicy_food_printer)
    #pass
#print_spicy_foods()

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
            if food["cuisine"] == cuisine:
                return(food)
    #pass
#get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods = spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spicy_food_printer = (f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
            print(spicy_food_printer)
    #pass

def get_average_heat_level(spicy_foods = spicy_foods):
    length = len(spicy_foods)
    index = length - 1
    sum = 0

    while(index >= 0):
        sum += spicy_foods[index]["heat_level"]
        index -= 1

    average_heat_level = (sum / length)
    return(average_heat_level)
    #pass
get_average_heat_level()

new_food = {
    "name": "French Fries",
    "cuisine": "French",
    "heat_level": 7
}
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return(spicy_foods)
    #pass
create_spicy_food(spicy_foods, new_food)