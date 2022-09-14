Max = int(input("Max waarde "))
Min = int(input("Min waarde "))

if Max > Min :
    print ("Max meer waard")
elif Max < Min:
    print("Min is meer waard dan Max")
else :
    print("Max en Min zijn gelijk aan elkaar")
print(f"Het minimum is {Min} Het maximum is {Max}")