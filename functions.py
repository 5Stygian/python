formulaOptions = '''
+-----------------+-------------+
|  Function Name  |  Shorthand  |
+-----------------+-------------+
|    Summation    |    1, sum   |
|    Formula2     |    2, f2    |
+-----------------+-------------+'''

def summation(lower_bound = 0, upper_bound = 1, formula = ""):
    while True:
        try:
            lower_bound = int(input("Lower bound: "))
            upper_bound = int(input("Upper bound: "))
            break
        except:
            lower_bound = int(input("Lower bound: "))
            upper_bound = int(input("Upper bound: "))
    for i in range(upper_bound): # loop through each itteration until upper bound in reached
        pass

def formula2(num1, num2):
    pass

def inputs(cColor, bgColor, formula):
    cColor  = inout("Turtle color: ")
    bgColor = input("Background color: ")
    print(f"{formulaOptions}")
    formula = input("Formula: ")
    crush.color(cColor)
    screen.bgcolor(bgColor)
    match formula:
        case "1":
           formula1() 
        case "2":
            formula2()
        case _:
            inputs()
