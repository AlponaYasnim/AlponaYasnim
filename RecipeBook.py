class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_details(self):
        print("Recipe: " + self.name)
        print("Ingredients:")
        for ingredient in self.ingredients:
            print("- " + ingredient)
        print("Instructions:")
        for i, instruction in enumerate(self.instructions, start=1):
            print(str(i) + ". " + instruction)
        print()


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def display_recipes(self):
        print("All Recipes:")
        for recipe in self.recipes:
            recipe.display_details()


# Example usage
recipe_book = RecipeBook()

recipe1 = Recipe("Pancakes",
                 ["1 cup flour", "2 tbsp sugar", "1 tsp baking powder", "1 cup milk", "1 egg"],
                 ["In a bowl, mix flour, sugar, and baking powder.",
                  "Add milk and egg, then mix until smooth.",
                  "Heat a lightly oiled griddle or frying pan over medium-high heat.",
                  "Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake.",
                  "Cook until bubbles form on the surface, then flip and cook until browned on the other side."])
recipe_book.add_recipe(recipe1)

recipe2 = Recipe("Spaghetti Bolognese",
                 ["1 lb ground beef", "1 onion, chopped", "2 cloves garlic, minced", "1 can diced tomatoes",
                  "1/2 cup tomato sauce", "1 tsp dried oregano", "1 tsp dried basil", "Salt and pepper to taste",
                  "8 oz spaghetti"],
                 ["In a large skillet, brown the ground beef over medium heat.",
                  "Add the chopped onion and minced garlic, and cook until the onion is tender.",
                  "Stir in the diced tomatoes, tomato sauce, oregano, basil, salt, and pepper.",
                  "Simmer for 20 minutes, stirring occasionally.",
                  "While the sauce is simmering, cook the spaghetti according to package instructions.",
                  "Serve the sauce over the cooked spaghetti."])
recipe_book.add_recipe(recipe2)

recipe_book.display_recipes()

recipe_book.remove_recipe(recipe1)

print("Updated Recipe Book:")
recipe_book.display_recipes()
