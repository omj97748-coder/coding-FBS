# write a program to calculate profit or loss.

cp = int(input("Enter cost price = "))
sp = int(input("Enter selling price = "))

if sp > cp:
    profit = sp - cp
    print("Profit = ",profit)
elif cp > sp:
    loss = cp - sp
    print("Loss = ",loss)
else:
    print("NO profit no loss")