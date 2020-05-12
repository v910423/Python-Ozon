import os

for file in os.listdir('/Users/valeriabelko/Desktop/Python'):
    if file.endswith('.txt'):
        print(file)


