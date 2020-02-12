def triangle(number):
    return_result = ''
    for column in range(number):
        for row in range(column + 1):
            print('#', end = ' ')
        print()
    return return_result

triangle_result1 = triangle(2)
triangle_result2 = triangle(4)

print(triangle_result1)
print(triangle_result2)