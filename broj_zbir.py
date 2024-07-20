x = int(input("Unesi x:"))
y = int(input("Unesi y:"))
z = int(input("Unesi z:"))
broj = 0
zbir = 0
for i in range(x,y+1):
    if i%z==0:
        broj+=1
        zbir+=i
print("Brojeva je",broj,"a njihov zbir je",zbir)
