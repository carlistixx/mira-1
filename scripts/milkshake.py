import sys

print("Welcome to the MILKSHAKE AND PANCAKE GAME!")
print("There is a kitty and a puppy. Who gets the milkshake?")


result = input("Press 1 for kitty and 2 for puppy: ")

if int(result) == 1:
    print("Kitty loves milkshakes! Purrrrrrr!!")
else:
    print("Puppy barfs because he hates milkshakes! Bleerrrrggggg!!")
    sys.exit(1)

print("Who gets the pancake?")
result = input("Press 1 for kitty and 2 for puppy: ")

if int(result) == 1:
    print("The kitty barfs because she hates pancakes! Bleerrrrggggg!!")
    sys.exit(1)
else:
    print("Puppy loves pancakes! Woof Woof!!")
        
