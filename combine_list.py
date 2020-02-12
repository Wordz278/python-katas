def merge(list1=[], list2=[]):    
    n = len(list1)
    store_list = []
    for i in range(n):
        store_list.append(list1[i])
        store_list.append(list2[i])
    return store_list

combined_list = merge([11,22,33], [1,2,3]) 
print(combined_list)
