def isosceles(number):
    initial_value = 0
    return_result = ''
    for column in range(1, number+1):
        for row in range(1, (number-column)+1):
            print(end="  ")
        while initial_value != (2*column-1):
            print("# ", end="")
            initial_value += 1
        initial_value = 0
        print()
    return return_result


result1 = isosceles(2)
result2 = isosceles(4)
print(result1)
print(result2)