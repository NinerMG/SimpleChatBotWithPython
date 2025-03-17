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

    def counting_numbers(self):
        number = int(input('Now I will prove to you that I can count to any number you want.'))
        for index in range(0, number + 1):
            print(f"{index} !")
        print('Completed, have a nice day!')

    def test(self):
        print("Let's test your programming knowledge.")
        print("Why do we use methods?")
        print("1. To repeat a statement multiple times.")
        print("2. To decompose a program into several small subroutines.")
        print("3. To determine the execution time of a program.")
        print("4. To interrupt the execution of a program.")

        while True:
            answer = int(input())
            if answer == 2:
                self.end()
                break;
            else:
                print("Please, try again.")

    def end(self):
        print('Congratulations, have a nice day!')