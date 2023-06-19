#Function that inserts the element into the indicated index. Return True if it has inserted the element and False otherwise

def insert_element(list, i, x):
    if i >= len(list):
        insert = False
    else:
        list.append(x)
        j = (len(list) - 2)
        while j >= i:
            list[j + 1] = list[j]
            j -= 1
        list[i] = x
        insert = True
    return insert

list_str= input("Enter the elements of the list: ").split()
i = int(input("Enter the index: "))
x = int(input("Enter a value to add: "))

list = []
for elem in list_str:
    m = int(elem)
    list.append(m)
print(insert_element(list, i, x))