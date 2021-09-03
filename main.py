"""Password generator"""

import random, string
from os import system
from time import sleep
        

CHARACTERS = string.hexdigits + string.punctuation


def generate_password(length: int, chars: string):
    """Generate password, return string"""
    arr = [random.choice(chars) for _ in range(length)]
    return ''.join(arr)


def get_characters():
    pass

def get_input(prompt: str):
    """Get userinput, return int"""
    try:
        return int(input(prompt))
        
    except ValueError:
        print('Invalid input')
        get_input(prompt)


def main():
    """Main function"""
    length = get_input('Please insert how many characters : ')
    password = generate_password(length, '')
    print(password)


if __name__ == '__main__':
    main()



