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

    def guess_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        remainder3 = int(input())
        remainder5 = int(input())
        remainder7 = int(input())
        your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        print(f"Your age is {your_age}; that's a good time to start programming!")