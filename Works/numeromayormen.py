
from random import randint, random
a=randint(0,100)
num= int(input("give me a number:"))
while num!=a:
    if   num > a:
        num=int(input("its too big give me a lower number: "))
    elif num < a:
        num=int(input("its to low give me a bigger number: "))
print("You got the number and it is :",a )

