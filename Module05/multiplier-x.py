
def aantal(number: int):
    for count in range(1, 11):
        print(f'{number}x{count} = {count*number}')

aantal(int(input('Van welk getal wil je de tafel zien? ')))