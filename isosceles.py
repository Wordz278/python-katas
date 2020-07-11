def isosceles(number):
    for row in range(1, number+1):
        print(" " * (number-row)+"# "*row)


if __name__ == "__main__":
    isosceles(4)
