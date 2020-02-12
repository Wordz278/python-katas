def even_or_odd(number):   
    if number%2 == 0:
        answer = f"{number} is a Even number"
    else:
        answer = f"{number} is a Odd number"
    return answer

result_even = even_or_odd(4)
result_odd = even_or_odd(3)

print(result_even)
print(result_odd)