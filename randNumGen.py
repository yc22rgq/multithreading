import sys
import random

def randNumGen():
    while True:
        command = input().strip()

        if command == "Hi":
            print("Hi")
        elif command == "GetRandom":
            print(random.randint(0, 100))
        elif command == "Shutdown":
            break
        else:
            continue


if __name__ == "__main__":
    randNumGen()