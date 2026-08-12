IsLoud = input("Is it loud? (True/False): ").strip().capitalize()

print("user input:", IsLoud)

if IsLoud == "True":
    print("This is loud!")
elif IsLoud == "False":
    print("This is quiet.")
else:
    print("I am not sure.")