def even_or_odd(number):
    if number % 2 == 0:
        answer = f"{number} is a Even number"
    else:
        answer = f"{number} is a Odd number"
    print(answer)
    return "done"


if __name__ == "__main__":
    even_or_odd(4)
    even_or_odd(3)
