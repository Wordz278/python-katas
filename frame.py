def frame(words=[]):
    size = len(max(words, key=len))
    print('*' * (size + 4))

    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
    return "done"


if __name__ == "__main__":
    frame(["Write", "good", "code", "everyday"])
