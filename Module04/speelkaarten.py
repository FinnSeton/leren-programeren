import random

SOORTKAART = ("harten ", "klaveren ", "schoppen ", "ruiten ")
NUMMERS_PLAATJES = ("aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer")
JOKER = ["joker", "joker"]

for a in SOORTKAART:
    for b in NUMMERS_PLAATJES:
        ab = a + b
        JOKER.append(ab)

random.shuffle(JOKER)

for i in range(1,8):
    print(f"kaar {i}: {JOKER[i]}")
    JOKER.pop(i)

print(f"aantal kaarten: {len(JOKER)} {JOKER}")