import re
print("Stupid Simple Calculator")
print("type 'quit' to exit\n")
previous = 0
run = True
def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:   
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation=='quit':
        run = False
    else: 
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else: 
            previous = eval(str(previous)+ equation) 
        # eval should be avoided because it can be dangerous
        # i.e. "eval "Hello world"
        # eval can evaluate any python code         


while run:
    performMath()
