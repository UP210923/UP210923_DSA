mon = int(input("Enter the amount of money: "))
t=1
count=0
while mon > t:
    mon-=t
    count+=1
    t+=1

print("You can get", count, "ticket(s)")
print("You stayed with $",mon)