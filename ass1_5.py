# take input for p & t & r
P = int(input('enter principal ammount :-'))
T = int(input('enter rate of interest:-' ))
R = int(input('enter time of year :-'))

# calculate amount 
total = P * (1 + R / 100)** T

# calculate compound interest
compound_interest = total - P

# display result 
print('compound interest is:', compound_interest)