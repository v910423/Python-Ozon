import json

numbers = [1,245,4,5,3,234,345,2345,1,3]

f = open('numbers.json', 'w')
json.dump(numbers, f)
f.close()