#first we print the first questions with input options
print("What's your name? ")

name = input("Enter name..")

print("Nice to meet you " + name + ".")
print("What year where you born? ")

thisYear = 2026
birthYear = input("Enter year you were born..")
age = thisYear - int(birthYear)

print("That would make you " + str(age) + " years old.")
print("What's your favorite food? ")

favFood = input("Enter favorite food..")

print("Oh I love " + favFood + ". It's soo tasty! ")
print("What's your favorite hobby?")

favHobby = input("Enter favorite hobby..")

print("I've always wanted to learn " + favHobby + ", it seems so interesting.")
print("What city are you from?")

hCity = input("Enter city name..")

print("Wow I've never been to " + hCity + " before. ")
print("Ok almost done")
print("What's your favorite person's name? ")

favPerson = input("Enter their name..")

print("How old are they?")

favPersonAge = input("Enter their age..")

print("Well you should have " + favPerson + " age " + int(favPersonAge) + " fill this out.")

monthsAlive = age * 12
leapDaysAlive = age / 4
daysAlive = age * 365 + leapDaysAlive
hoursAlive = daysAlive * 24
minAlive = hoursAlive * 60
secAlive = minAlive * 60
# on part 10 of assignment


print("Enough questions now, ")