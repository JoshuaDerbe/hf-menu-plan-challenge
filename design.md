# The Design

![alt text](https://github.com/JoshuaDerbe/hf-menu-plan-challenge/blob/main/diagrams/menu-plan-ER.png "ER Diagram")

Above is the ER diagram for the system. I thus identified the tables in the database to be:

-   User - represents users of the system (admins + customers). Contains email, hashed password and roles of the user.
-   Ingredient - represents ingredients e.g. Potato, Tomato, etc. Contains its name and nutritional values.
-   Allergen - holds the relationship between ingredients and allergens, which is a multi valued attribute. e.g. dairy, egg, gluten, etc. Contains a foreign key to ingredient and the allergen as a string.
-   Recipe - represents recipes which are semantically collections of ingredients with steps. This table itself contains only the name of the recipe, its steps, prep time, and difficulty.
-   InRecipe - holds the relationship between ingredients and recipes, i.e. what ingredients are on certain recipes and how much of the ingredient to use. Contains a foreign key to an ingredient, a foreign key to a recipe, and the measurement of this ingredient as a string.
-   Menu - represents menus which are semantically collections of recipes. Contains a name, and the starting and ending date of the menu.
-   OnMenu - holds the relationship between menus and recipes, i.e. what recipes are on certain menus. Contains a foreign key to a menu and a foreign key to a recipe.
-   RecipeReview - holds a review made by users for a specific recipe. Contains a foreign key to a user, a foreign key to a recipe, a comment as a string, and a rating as an integer between 1 and 5. At least one of comment and rating cannot be NULL.
-   MenuReview - holds a review made by users for a specific menu. Contains a foreign key to a user, a foreign key to a menu, a comment as a string, and a rating as an integer between 1 and 5. At least one of comment and rating cannot be NULL.

# Routes

## User Routes

### POST /api/signup/

Route for creating new users.

-   Expected request format: { email: str, password: str }
-   Successful response format: { results: {id: user.id, email: user.email} }
-   Results: New user in database with email and password given in request

### POST /api/login/

Route for logging in as a user, and receving an access token to use in future requests.

-   Expected request format: { email: str, password: str }
-   Successful response format: { access_token: access_token, roles: user.roles}
-   Results: No impact on the database

### DELETE /api/users/<u_id> - Auth required: admin

Route for deleting users.

-   Expected request format: valid id in url
-   Successful response format: "Successfully deleted user with id u_id!"
-   Results: user with id u_id removed from database, and can no longer login

## Ingredient Routes

### GET /api/ingredients/ - Auth required

Route for obtaining all the ingredients in the database.

-   Expected request format: N/A
-   Successful response format: { results: [ { id: ingredient.id, name: ingredient.name, energy: ingredient.energy, ... }, ... ] }
-   Results: No impact on the database

### POST /api/ingredients/ - Auth required

Route for obtaining ingredients with specific ids from the database.

-   Expected request format: { ids: [ str, ... ]}
-   Successful response format: { results: [ { id: ingredient.id, name: ingredient.name, energy: ingredient.energy, ... }, ... ] }
-   Results: No impact on the database

### POST /api/ingredients/add - Auth required: admin

Route to add an ingredient to the database.

-   Expected request format: { name: str, energy: (int >= 0)}
-   Successful response format: { results: { id: ingredient.id, name: ingredient.name, energy: ingredient.energy, ... } }
-   Results: new ingredient with name and energy values given in the request added to the database

### POST /api/ingredients/edit - Auth required: admin

Route to update an ingredient in the database.

-   Expected request format: { id: str, (optional: name: string, energy: int)}
-   Successful response format: { results: { id: ingredient.id, name: ingredient.name, energy: ingredient.energy, ... } }
-   Results: ingredient with id given in the request is changed to have the name given in the request, and the energy given in the request (if the new name is unique)

### DELETE /api/ingredients/<i_id> - Auth required: admin

Route to remove an ingredient from the database.

-   Expected request format: valid id in url
-   Successful response format: "Successfully deleted ingredient with id i_id!"
-   Results: ingredient with id i_id removed from database
