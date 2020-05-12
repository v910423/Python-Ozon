def count_words(filename):

    try:
        file = open(filename, encoding='utf-8')
        content = file.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f'в этом {filename} около {num_words} слов')




filenames = ['1.txt', '2.txt', '3.txt']
for filename in filenames:
    count_words(filename)