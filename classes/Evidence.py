from .Person import Person

class Evidence:
    def __init__(self):
        # Array se všemi pojištěncemi
        self.policyholders = []

    def menu(self):
        print("\nVyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("0 - Konec\n")

        while True:
            try:
                choice = int(input("Zadej výběr: "))
            except ValueError:
                print("Nevalidní volba - výběr musí být číslo")
                continue
            else:
                if choice < 0 or choice > 3:
                    print("Nevalidní volba - zadejte číslo z menu")
                    continue
                else:
                    return choice

    def addPolicyholder(self):
        firstname = input("Zadej jméno pojištěného:\n")
        surname = input("Zadej příjmení pojištěného:\n")
        age = None
        # Vyžaduje věk dokud uživatel nezadá validní kladné číslo
        while True:
            try:
                age = int(input("Zadej věk:\n"))
            except ValueError:
                print("Věk musí být kladné číslo")
                continue
            else:
                if age <= 0:
                    print("Věk musí být kladné číslo")
                    continue
                else:
                    break

        number = None
        while True:
            number = input("Zadej telefonní číslo:")
            # Telefonní číslo musí být 9 znaků dlouhé číslo
            if number.isnumeric() and len(number) == 9:
                break
            else:
                print("Neplatné telefonní číslo")
                continue
        self.policyholders.append(Person(firstname, surname, age, number))
        print("Nový pojištěnec přidán.")
        input("Pokračujte libovolnou klávesou...\n")

    def printEvidence(self):
        for person in self.policyholders:
            print(person)
        input("Pokračujte libovolnou klávesou...\n")

    def search(self):
        searchString = input("Zadejte hledané jméno nebo příjmení:\n")
        for person in self.policyholders:
            if person.firstname == searchString or person.surname == searchString:
                print(person)
        input("Pokračujte libovolnou klávesou...\n")
