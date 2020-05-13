from datetime import datetime
import os

start = input('If you want to start diary, press Y: ').upper().strip()

if start != 'Y':
    exit()

while True:
    path = input('Choose directory where you want to keep notes: ')  #/Users/valeriabelko/Desktop/
    if os.path.exists(path):
        os.chdir(path)
        break

try:
    os.mkdir('Diary')
except FileExistsError:
    pass
os.chdir(path + '/Diary')

currdate = input('Enter date. If it is current day, press T. ').upper().strip()
if currdate == 'T':
    currdate = datetime.now().date()

folder_name = str(currdate)

try:
    os.mkdir(folder_name)
except FileExistsError:
    print('nope')

os.chdir(path + 'Diary/' + folder_name)
descr = str(input('What happened this day?: '))
currtime = datetime.now().strftime('%H:%M_%d.%m.%y')
print(currtime)

with open(currtime + ".txt", 'w') as file:
    file.write(descr)

