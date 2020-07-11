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
    print("\n".join(returnlist))
    return "done"


if __name__ == "__main__":
    longest_word(["the", "quick", "brown", "fox", "ate", "my", "chickens"])
    longest_word(["once", "upon", "a", "time"])
