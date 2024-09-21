"""
Exercise 18
Calculate the distance of two points A = (3, 2), B = (- 1, -1) and 
print result to the console as shown below.

Expected result:
The distance between points A and B: 5.0
"""

a1 = 3
a2 = 2
b1 = -1
b2 = -1

distance = ((b1 - a1) ** 2 + (b2 - a2) ** 2)**(1/2)

print(f'The distance between points A and B: {distance}')
