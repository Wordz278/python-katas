def longest_word(long_word=[]): 
    sentence = long_word
    length = []
    for max_word_length in sentence:
        length.append(len(max_word_length))
    maximum = max(length)
    returnlist = []
    for max_word in sentence:
        if len(max_word) == maximum:
            returnlist.append(max_word)
            list_word = max_word
    return list_word

long_word_result= longest_word(["the","quick","brown","fox","ate","my","chicken"])
print(long_word_result)
