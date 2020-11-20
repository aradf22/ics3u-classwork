colour = (input("What's your favorite colour? "))
print("Really? I hate ", colour)


cans = int(input("How many cans come in 1 package? "))
pack = int(input("How many packs are there? "))
num = cans * pack
print ("You have purchased a total of", num, "cans ")


base = int(input("What's the length of the base of the prism? In meters: "))
width = int(input("What's the width of the prism? In meters: "))
height = int(input("What's the height of the prism? In meters: "))
volume = base * width * height
print("If those are all true, then your prism should have a volume of", volume, "meters cubed")
