def triangle():
    num = int(input("Enter the triangle measures : "))
    for i in range(num):
        for j in range(i + 1):
            print('#', end = ' ')
        print()

triangle()