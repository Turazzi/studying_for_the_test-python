#Function that removes the element from the given index. The function should return True if it removed the element and False if it didn´t

def remove_index(list, i):
    if i >= len(list) and i < 0:
        remove = False
    else:
        j = i
        while j < len(list) and (j + 1) < len(list):
            list[j] = list[j + 1]
            j += 1
        list.pop()
        remove = True
    return remove

list_str= input("Enter the elements of the list: ").split()
i = int(input("Enter the index: "))

list = []
for elem in list_str:
    m = int(elem)
    list.append(m)

print(remove_index(list, i))