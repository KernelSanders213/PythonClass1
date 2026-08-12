
# create a total varible
# for loop to add both to total 5 times
variable1 = 1
variable2 = 2
total = 0
for count in range(5): # Executes 5 times
    print("total =", total, "+ (" , variable1, "+", variable2,")")
    total += (variable1 + variable2)
    print("total =",total)

print(total)
# total = 0 + (1 + 2) # total = 3
# total = 3 + (1 + 2) # total = 6
# total = 6 + (1 + 2) # total = 9
# total = 9 + (1 + 2) # total = 12
# total = 12 + (1 + 2) # total = 15
