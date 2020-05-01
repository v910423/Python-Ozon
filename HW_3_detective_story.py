#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машинной марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo'}

#print(type(shevrole_owner))

a = shevrole_owner & work_near & live_near
b = shevrole_owner & work_near
c = shevrole_owner & live_near
d = work_near & live_near

#quest = input("If you want to define those who live and work near places of crime, type 1: ")
#print(list(live_near) + list(work_near))
# asd = work_near | live_near
# print(asd)
print((work_near | live_near) & shevrole_owner)