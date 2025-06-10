# ROUNDOFF FUNCTION
# this function roundsoff the float number after the point till the given roundoff limit
# syntax of roundoff func is--> round(number, n digit roundoff limit )
x=float(input("enter x "))
y=float(input("enter y "))
print(round(x+y,2))

## WE CAN ALSO USE FLOOR METHOD INSTEAD TO FIND GIF
print(x//y)

# international numbering system
# to add commas as in international system we use this method
z=798563
print(f"{z:,}")

# division and rounding off
#syntax of the rounding in dividing is print(f"{z:.2f}") or print(round(num,digit))
z=round(x/y,2)
print(z)
print(f"{z:.2f}")
