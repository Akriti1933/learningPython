#empty list
#[-]= to last value
#print(list_fruits[-2])
empty_list = []

list_fruits = ["Apple","Bananana","Orange"]

#to change index
list_fruits[0]="mango"


#to insert
list_fruits.append("kiwi")

#to remove
list_fruits.remove("kiwi")

#print(list_fruits)



list_marks =[18,23,45,33]

#mixed list
mixed_list = ["Apple",True ,18]

#print(mixed_list)

#loop in list
#for fruit in list_fruits:
    #print(fruit)

    #range
#for i in range( len(list_fruits)):
   # print(f'{i} : {list_fruits[i]}')

   # to sort
#list_fruits.sort()

#to reverse
list_fruits.reverse()
print(list_fruits)

index_of_apple=list_fruits.index('mango')
print(index_of_apple)