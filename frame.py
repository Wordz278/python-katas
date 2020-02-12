def frame(words=[]):
    result_empty = ''
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
    return result_empty

sentence = frame(["Write", "good", "code", "everyday"])

