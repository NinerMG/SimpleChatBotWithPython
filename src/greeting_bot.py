class Greeting_Bot:

    def __init__(self, bot_name, creation_year):
        self.bot_name = bot_name
        self.creation_year = creation_year
        self.greet()

    def greet(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.creation_year}.")

    def remind_name(self):
        name = input("Please, remind me your name.")
        print(f"What a great name you have, {name}!")