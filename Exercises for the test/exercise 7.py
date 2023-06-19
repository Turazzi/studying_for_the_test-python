#Function that takes two lists and returns True if they are equal and False otherwise

def equal_lists(list1, list2):
    if list1 == list2:
        iguais = True
    else:
        iguais = False
    return(iguais)

l1 = input("Enter the elements of l1: ").split()
list1 = []
for elem in l1:
    m = int(elem)
    list1.append(m)

l2 = input("Enter the elements of l2: ").split()
list2 = []
for elem in l2:
    m = int(elem)
    list2.append(m)

print(equal_lists(list1, list2))