uur = 0
ap = 'AM'	
while uur <= 24:
    print (ap, uur, '00')
    if uur <= 12:
        ap = 'AM'
    if uur >= 12:
        ap = 'PM'
    uur = uur + 1 
        
    