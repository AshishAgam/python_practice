# continue statement in python
i = 0
while i <= 5:
    if(i ==3):
        i +=1
        continue # skip 3
    print(i)
    i +=1
    
# Print only even number
i = 1
while i <= 10:
    if (i%2 != 0):
        i +=1
        continue # skip odd numbers
    print(i)
    i +=1
