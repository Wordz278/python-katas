def square():
    num = int(input("Enter the square size : "))
    for i in range(num): #rows - outer loop
        for j in range(num): #number of spaces
            print('#', end='')
        print()

square()