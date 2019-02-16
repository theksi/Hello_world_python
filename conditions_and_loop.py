# check = False
# if check == False:
#    print("it is false")
# else :
#    print("it is true")

check = "Hamburger"
if check == False:
    print("it is false")
elif check == "Hamburger":
    print("yummmm")
elif check == "Yo":
    print("Hello")
else :
    print("it is true")
# FOR LOOP 
# usefull for Arrays
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

# While loop
run = True
current = 1
while run:
    if current == 100:
         run = False
    else:
            print(current)
            current += 1
