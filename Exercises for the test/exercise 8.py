#Function that takes two lists and returns True if they have the same elements in the same quantity and False otherwise

def elem_lists(list1, list2):
    counter_l1 = 0
    i = 0
    same_amount = True
    if len(list1) != len(list2):
        same_amount = False
    else:
        for i in range(len(list1)):
            for j in range(len(list1)):
                if list1[i] == list2[j]:
                    counter_l1 += 1
    if counter_l1 != len(list1):
        same_amount = False
        return(same_amount)
    return(same_amount)

l1 = input("Enter the elements of list 1: ").split()
list1 = []
for elem in l1:
    m = int(elem)
    list1.append(m)

l2 = input("Enter the elements of list 2: ").split()
list2 = []
for elem in l2:
    m = int(elem)
    list2.append(m)

print(elem_lists(list1, list2))