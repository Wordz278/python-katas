def longest_word(word): 
    print("The longest word is : ")
    words = list(word.split(" "))
    length = []
    for i in words:
        length.append(len(i))
    maximum = max(length)
    returnlist = []
    for j in words:
        if len(j) == maximum:
            returnlist.append(j)
            list_word = j
            print(list_word)
            
longest_word(input("Enter the Desired Sentence : "))
