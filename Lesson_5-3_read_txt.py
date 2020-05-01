with open("/Users/valeriabelko/Desktop/new2.txt") as file:
    # text = file.read()
    # print(text)
    # content = file.read().split('\n')
    # print(type(content))

    for line in file:
        lines = file.read().split('\n')
        print(line)