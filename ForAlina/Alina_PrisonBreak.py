original_list = [1, 1, 0, 0, 0, 1, 0]
inverted_list=[]
for c in original_list:
    if c==0:
        inverted_list.append(1)
    else:
        inverted_list.append(0)

list = original_list
is_inverted = False
c=0
for x in range(0,len(list)):
    if list[x]==1:
        c+=1
        if(is_inverted):
            list = original_list
            is_inverted = False
        else:
            list = inverted_list
            is_inverted = True

print(c)

