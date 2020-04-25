name = input("What is your name?\n")
print("Hi,", name)
gender = input("Are you a boy or a girl?\n")
gender = gender.strip()

if gender == "boy":
    print("You have short black hair")
elif gender == "girl":
    print("You have golden long pig tails with pink bows at the end")
else:
    print("Sorry, that is not a choice. Start over!")

color = input("what is your favorite color\n?")
if gender == "girl":
    print( "you are wearing a %s dress" % color) 
if gender == "boy":
    print( "you are wearing a %s shirt" % color)

