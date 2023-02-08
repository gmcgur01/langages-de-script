#! /usr/bin/env python3
import random

def main():
    Deviner(5)

def Deviner(k):
    
    nombre = random.randint(0,k)

    while True:
        try:
            guess = int(input("Devinez un nombre: "))
        except ValueError:
            print("Proposez uniquement des nombres entiers.")
            continue
        except KeyboardInterrupt:
            print("\nLe nombre était", nombre, "!")
            break

        if guess > nombre:
            print("Nombre trop grand.")
        elif guess < nombre:
            print("Nombre trop petit.")
        else:
            print("Bravo !")
            break

    print("Au revoir")

if __name__ == "__main__":
    main()