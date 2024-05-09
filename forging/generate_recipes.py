# generate_recipes.py: takes in a CSV file from Leif's spreadsheet and generates the SQL commands and recipe.txt file lines

# convert Leif's spreadsheet into a JSON dictionary
def get_recipe_dict_from_file(filename):
    recipes = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            elements = line.replace("\n", "").split(",")
            recipe_id = elements[1]
            recipes[recipe_id] = {}
            name = elements[0]
            recipes[recipe_id]["name"] = name
            classes = elements[2].split("/")
            recipes[recipe_id]["class"] = classes
            level = elements[3]
            recipes[recipe_id]["level"] = level
            item_id = elements[4]
            recipes[recipe_id]["item"] = item_id
            craft_type = elements[5].lower()
            recipes[recipe_id]["type"] = craft_type
            location = elements[6]
            recipes[recipe_id]["location"] = location
            # ingredients
            recipes[recipe_id]["ingredients"] = {}
            i = 7+2  # starting point for recipes, +3 so at the end
            while i < len(elements):
                if elements[i] != "":
                    ingredient_id = elements[i-1]  # get item ID
                    ingredient_quantity = elements[i]  # get item amount
                    recipes[recipe_id]["ingredients"][ingredient_id] = ingredient_quantity
                i += 3  # move to next item
    print("Completed parsing " + filename + " into a recipy dictionary.")
    return recipes

# generate the recipe SQL
def generate_sql_from_recipe_dict(recipes_dict, craft="forging"):
    sql = []
    for recipe_id in recipes_dict:
        recipe = recipes[recipe_id]
        # uses the recipe ID for the cost ID
        # get the vendor corresponding to the area
        if recipe["type"] == "forging":
            vendor = "494" if recipe["location"] == "Farcrag" else "495" if recipe["location"] == "Shalemont" else "496" if recipe["location"] == "Stonevale" else "497" if recipe["location"] == "Otherworld" else "498" if recipe["location"] == "Carrowmore" else "499" if recipe["location"] == "Tower" else "494"
        if recipe["type"] == "alchemy":
            vendor = "489" if recipe["location"] == "Dustwither" else "490" if recipe["location"] == "Tavern" else "491" if recipe["location"] == "Otherworld" else "492" if recipe["location"] == "Carrowmore" else "493" if recipe["location"] == "Gardens" else "489"
        if recipe["type"] == "crafting":
            vendor = "484" if recipe["location"] == "Crookback" else "485" if recipe["location"] == "Fingals" else "486" if recipe["location"] == "Sewers" else "487" if recipe["location"] == "Carrowmore" else "488" if recipe["location"] == "Gardens" else "484"
        # recipes table
        sql.append("DELETE FROM `recipes` WHERE `recipe_name`='" + recipe["name"] + "'; INSERT INTO `recipes` (`recipe_name`, `success_min_chance`, `success_max_chance`, `critical_min_chance`, `critical_max_chance`, `master_min_chance`, `master_max_chance`, `min_ability`, `difficulty`, `recipe_level`, `recipe_xp`, `failure_item_reward`, `success_item_reward`, `critical_item_reward`, `master_item_reward`, `crafting_time`, `recipe_id`, `cost_id`, `optional_item_id`, `food_mesh_type`) VALUES ('" + recipe["name"] + "', 100, 100, 0, 0, 0, 0, 0, 0, " + recipe["level"] + ", 100, 1, " + recipe["item"] + ", 1, 1, 9, " + recipe_id + ", " + recipe_id + ", -1, NULL);")
        # token vendor stock table
        sql.append("DELETE FROM `token_vendor_stock` WHERE `token_vendor_stock_id`=" + recipe_id + ";")
        sql.append("INSERT INTO `token_vendor_stock` (`token_vendor_stock_id`, `token_vendor_id`, `item_template_id`, `token_vendor_cost_id`) VALUES (" + recipe_id + ", " + vendor + ", " + recipe["item"] + ", " + recipe_id + ");")
        # token vendor cost table
        sql.append("DELETE FROM `token_vendor_cost` WHERE `token_vendor_cost_id`=" + recipe_id + ";")
        for ingredient_id in recipe["ingredients"]:
            ingredient_quantity = recipe["ingredients"][ingredient_id]
            sql.append("INSERT INTO `token_vendor_cost` (`token_vendor_cost_id`, `item_template_id`, `quantity`) VALUES (" + recipe_id + ", " + ingredient_id + ", " + ingredient_quantity + ");")

    # save the sql
    with open("recipe_sql_update.txt", "w") as f:
        for cmd in sql:
            f.write(cmd + "\n")
        print("Generated recipe_sql_update.txt, run the file contents and it will delete the existing recipes and insert the new ones.")
    return sql

# generate the recipe txt file
def generate_txt_from_recipe_dict(recipes_dict):
    txt = []
    for recipe_id in recipes_dict:
        recipe = recipes[recipe_id]
        # uses the recipe ID for the cost ID
        txt.append(recipe["name"] + ",100,100,0,0,0,0,0,1," + recipe["level"] + ",100,-1," + recipe["item"] + ",-1,-1,9," + recipe_id + "," + recipe_id + ",-1,2")

    with open("recipe_txt_update.txt", "w") as f:
        for cmd in txt:
            f.write(cmd + "\n")
    print("Generated recipe_txt_update.txt, replace the associated lines of recipes.txt with this file's contents.")
    return txt

recipes = get_recipe_dict_from_file("crafting.csv")
generate_sql_from_recipe_dict(recipes)
generate_txt_from_recipe_dict(recipes)