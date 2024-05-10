number_list = []

print("Enter number :")
item = int(input())
i = 0
while (item!=-1):
    number_list.append(item)
    print("Enter next number :")
    item = int(input())
    i+=1

average = sum(number_list)/i

print("The average is: ", average)