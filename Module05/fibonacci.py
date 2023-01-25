def fibonacci(nummer: int):
    nummer_reeks = [0, 1]
    gebruiker_reeks = []
    for x in range(0, 50):
        nummer_reeks.append(nummer_reeks[-2] + nummer_reeks[-1])

    if nummer not in nummer_reeks:
        print(f"{nummer} zit iet in de reeks")
    elif nummer in nummer_reeks:
        for x in range(0, len(nummer_reeks)):
            if nummer_reeks[x] == nummer:
                for y in range(x, x + 10):
                    gebruiker_reeks.append(nummer_reeks[y])
    return gebruiker_reeks

print(fibonacci(55))

def fibonacci(nummer: int):
    nummer_reeks = [0, 1]

    for x in range(0, 100):
        nummer_reeks.append(nummer_reeks[-2] + nummer_reeks[-1])

    if nummer not in nummer_reeks:
        print(f"{nummer} zit niet in de reeks")
    elif nummer in nummer_reeks:
        print(nummer_reeks[0:nummer_reeks.index(nummer) + 1])

fibonacci(0)