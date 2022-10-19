import time
for tijd in range(0, 24):
    time.sleep(0.1)
    if tijd < 12:
        pa = ('AM')
    else:
        pa = ('PM')
    print(pa, tijd, ':00 uur')
    for minuut in range(0, 60):
        print(pa, tijd, ':', minuut)
    print()