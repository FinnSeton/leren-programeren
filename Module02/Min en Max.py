a = input('A: voer een getal in:')
b = input('B: voer een getal in:')

if a > b: 
    max=a
    min=b
    print(max, 'is groter dan', min)

elif a < b:
    min = a
    max = b
    print(min ,'is kleiner dan', max)

else :
    print(a, 'is gelijk aan' ,b)
