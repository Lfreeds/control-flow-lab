# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


a = int(input("Enter the first length of a triangle: "))
b = int(input("Enter the second length of a triangle: "))
c = int(input("Enter the third length of a triangle: "))

if a == b and a == c:
    type = "Equilateral"
    print(f"A triangle with side of {a}, {b} and {c} is a {type}")
elif a == b or a == c or b == c:
    type = "Scalene"
    print(f"A triangle with side of {a}, {b} and {c} is a {type}")
else:
    type = "Isosceles"
    print(f"A triangle with side of {a}, {b} and {c} is a {type}")