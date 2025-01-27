""" Name: Patricia Gariando
    Student Number: 991 446 494
    Task: Assignment 1
    Date: Sept 30 2023 """

# list of multilined messages 
shapeMenu = """
- + - + - + - + - + -
- SHAPE CALCULATION -
- + - + - + - + - + - 
- - - - - - - - - - -
-    1. Triangle    -
-    2. Rectangle   -
-    3. Circle      -
- - - - - - - - - - -"""

colorMenu = """
- + - + - + - + - + -
-    SHAPE COLOR    -
- + - + - + - + - + -
- - - - - - - - - - -
-      1. Red       -
-      2. Blue      - 
-      3. Green     -
- - - - - - - - - - -"""

negativeShape = """
~ ~ ~ ~ ~  W A R N I N G  ~ ~ ~ ~ ~
  ~ Negative shape not allowed! ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"""

invalidShape = """
~ ~ ~ ~ ~ W A R N I N G ~ ~ ~ ~ ~
    ~ Invalid shape choice! ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"""

finalOutput = """
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
You have chosen a %s %5s 
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"""

# display the title and options to the user 
print(shapeMenu)
shapeNum = int(input("Choose your shape: "))

if shapeNum < 0: 
    print(negativeShape)
elif shapeNum == 0 or shapeNum > 3:
    print(invalidShape)
else:
    if shapeNum == 1: # option 1 
        shape = "Triangle"
        # prompt the user 
        print()
        triHeight = int(input("Enter the height of the triangle: "))
        triBase = int(input("Enter the base length of the triangle: "))
        # calculate and display
        triArea = 0.5 * triHeight * triBase
        print("The area of the triangle is: ", triArea)

    elif shapeNum == 2: # option 2 
        shape = "Rectangle"
        # prompt the user 
        print()
        rectWidth = int(input("Enter the width of the rectangle: "))
        rectLength = int(input("Enter the length of the rectangle: "))
        # calculate and display
        rectArea = rectLength * rectWidth
        rectPerimeter = 2 * (rectLength + rectWidth)
        print("The area of the rectangle is: ", rectArea)
        print("The perimeter of the rectangle is: ", rectPerimeter)

    else: # option 3  
        shape = "Circle"
        # prompt the user 
        print()
        cirRadius = int(input("Enter the radius of the circle: "))
        # calculate and display
        cirDiameter = 2 * cirRadius
        print("The diameter of the cicle is: ", cirDiameter)  

    # this block only excutes when the user meets one of the three conditions above 
    print(colorMenu) # display the title and options to the user 
    colorNum = int(input("Choose your color: ")) # prompt the user

    if colorNum < 0: 
        print(negativeShape)
    elif colorNum == 0 or colorNum > 3:
        print(invalidShape)
    else:
        if colorNum == 1:
            color = "Red"
        elif colorNum == 2:
            color = "Blue"
        else:
            color = "Green"
        print(finalOutput %(color, shape))    
# displays name and student ID number every time the program is run                
print()
print("Patricia Gariando: 991 446 494") 
print()