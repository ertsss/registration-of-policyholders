from classes.Evidence import Evidence


def mainLoop():
    evidence = Evidence()
    while True:
        # Zobrazí menu s volbou akce
        choice = evidence.menu()
        if choice == 0:
            print("\n\nUkončuji...")
            break
        elif choice == 1:
            evidence.addPolicyholder()
        elif choice == 2:
            evidence.printEvidence()
        else:
            evidence.search()


if __name__ == '__main__':
    print("----------------------------")
    print("Evidence pojištěných")
    print("----------------------------")
    mainLoop()
