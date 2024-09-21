"""
Exercise 23
From the given file name:
filename = 'view.jpg'
extract extension and print it to the console.

Expected result: jpg
"""
# below solution with slicing
filename = 'view.jpg'
result = filename[-3:]
print(result)
# Below logic works for any extension having there or different number of characters after dot
# case-1

filename = 'view.jpg'
result = filename.split('.')[1]
print(f'result: {result}')


#case-2
filename = 'view.jpeg'
result = filename.split('.')[1]
print(f'result: {result}')
