def merge():
    list1 = []
    list2 = []
    
    lst1 = input("Enter numbers for list 1 : ").split(" ")
    list1 = lst1
    
    lst2 = input("Enter numbers for list 2 : ").split(" ")
    list2 = lst2

    n = len(list1)
    store_list = []
    for i in range(n):
        store_list.append(list1[i])
        store_list.append(list2[i])
    print(store_list)
merge()
