year=2000
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")


list1 = ["","",""]
list2 = ["","",""]
list3 = ["","",""]
index_list = ["a","b","c"]
final_list = [list1,list2,list3]

user_input = input("where to?--")

letter_index = index_list.index(user_input[0])
number_index = int(user_input[1])-1
final_list[number_index][letter_index]="something"

print(f"{list1}\n{list2}\n{list3}")