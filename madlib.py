name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
number = input("Enter a number: ")
food = input("Enter a food: ")

def tell_story(name, adjective, animal, place, number, food):
    story = "Once upon a time, " + name + " went for a walk in " + place + ".\n" \
    + "Suddenly, " + name + " found a " + adjective + " " + animal + "!\n" \
    + "The " + animal + " said it was exactly " + str(number) + " years old,\n" \
    + "and it only ate " + food + " for breakfast.\n" \
    + name + " could not believe it, and they became best friends.\n" \
    + "THE END."
    return story

print(tell_story(name, adjective, animal, place, number, food))
 