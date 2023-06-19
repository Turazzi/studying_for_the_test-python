#A function that takes a list as parameter and returns True if the list sorted in ascending order

def dropdown_list(list):
    
    lower = list[0]
    increasing = True
    
    for i in range(len(list)):
    
        if lower < list[i]:
            lower = list[i]
        elif lower > list[i]:
            increasing = False
        return(increasing)
        
    return(increasing)

list = list(map(int, input("Enter the elements of the list: ").split()))

print(dropdown_list(list))

