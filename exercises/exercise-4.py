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

a = input("Enter side a of the triangle: ")
b = input("Enter side b of the triangle: ")
c = input("Enter side c of the triangle: ")

if a == b and b == c:
    t_type = "equalateral"
elif a == b or b == c or a == c:
    t_type = "isosceles"
else:
    t_type = "scalene"

print(f"A triangle with sides of {a}, {b} & {c} is: {t_type}")