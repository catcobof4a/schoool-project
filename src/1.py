import random
class RandomPythonCode:
    def get_random_code(self):
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        if num % 2 == 0:
            return "print('even number')"
        else:
            return "print('odd number')"