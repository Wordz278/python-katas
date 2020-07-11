def combine(list1=[], list2=[]):
    n = len(list1)
    store_list = []
    for i in range(n):
        store_list.append(list1[i])
        store_list.append(list2[i])
    print(store_list)
    return "done"


if __name__ == "__main__":
    combine([11, 22, 33], [1, 2, 3])
