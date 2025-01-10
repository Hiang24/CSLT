str=input('str=')
ch=input('ch=')
str=str.lower()
ch=ch.lower()
dem=0
for i in str:
    if i==ch:
        dem+=1
print(f'Number of character {ch} is: {dem}')