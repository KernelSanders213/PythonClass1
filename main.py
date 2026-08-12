name = input("Enter your name: ")
age = int(input("Enter your age: "))

# If age is 65 there are 6 conditionals that wll be checked.

if age < 18:
    print(f"Hello {name}, you are a minor.")
elif age >= 18 and age < 30:
    print(f"Hello {name}, you are a young adult.")
elif age >= 30 and age < 50:
    print(f"Hello {name}, you are a middle adult.")
elif age >= 50:
    print(f"Hello {name}, you are a senior.")

# More efficient way to write. They are the same as the above code but more efficient. 
# The elif statements are not needed to check for the lower bound
# because if the age is less than 18, it will not reach the elif statements.

# if the age is 65 there are 3 conditionals that will be checked.

if age < 18: 
    print(f"Hello {name}, you are a minor.")
elif age < 30: # Greater than or equal to 18 and less than 30
    print(f"Hello {name}, you are a young adult.")
elif age < 50: # Greater than or equal to 30 and less than 50
    print(f"Hello {name}, you are a middle adult.")
else: # Greater than or equal to 50
    print(f"Hello {name}, you are a senior.")