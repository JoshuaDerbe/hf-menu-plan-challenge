# hf-menu-plan-challenge
# The Task
The task can be found [here](https://github.com/hello-abhishek/hf-take-home-programming-challenges/blob/main/SOFTWARE-ENGINEER.md)
# The Design
Detailed information on the design can be found [here](https://github.com/JoshuaDerbe/hf-menu-plan-challenge/blob/main/design.md)
# Setup Instructions
1. Clone the repository to your local machine
2. Ensure you have docker installed on your local machine, including docker-compose.
3. From the home directory of the repository, run the command: `docker-compose up --build`
4. The API and database should now be running. You should be able to issue API calls to http://localhost:5000/api/ on your local machine to get results.
5. To run it in the future, run the command: `docker-compose up` instead of using the `--build` flag.
#### NOTES
* To reset the database, delete/trash your docker container and run `docker-compose up --build` again.
# Running Tests
## Make sure you have pytest and newman/Postman installed to run the tests!
To run the tests, run the bash script `./runTests.sh`.
* You will need pytest and newman installed for the script to work. 
* The docker container must be running for the tests to pass.
* Alternatively to run the tests in isolation, cd to the backend folder and run `python3 -m pytest` to run the unit tests, and run `newman run backend/tests/postman/hf_menu_plan.postman_collection.json` to run the E2E tests.
* Alternatively to run the E2E tests you can import the hf_menu_plan.postman_collection.json file into Postman and run the collection from there.
#### NOTES
* The unit tests in pytest are extremely basic and not extensive. I could not get a clean testing database for pytest to interact with to work in time, so I could not create unit tests to check changes to the database. The basic pytests are still there to show I know what pytests are, what they are used for, and how to create them.
# Things not completed/TODO
* Add the routes (to create, list, read, update and delete) for the models apart from Ingredient and User. E.g. Recipe, Menu, Reviews, etc.
* Add more helper routes for users and ingredients.
* More extensive unit/E2E tests.
