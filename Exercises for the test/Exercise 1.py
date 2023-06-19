#Function that returns the first position that the element is found. If its not found, return -1

def first_position(list, x):
    for i in range(len(list)):
        if x == list[i]:
            return i
    return -1

list_str= input("Enter the elements of the list: ").split()
x = int(input("Enter x: "))

list = []
for elem in list_str:
    m = int(elem)
    list.append(m)

print(first_position(list, x))