#Function that returns if the string is composed only of different characters

def different_characters(list):

    characters = True
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
        
            if list[i] == list[j]:
                characters = False
            return(characters)

    return(characters)

list = input("Enter a string: ")

res = different_characters(list)

if res:
    print("It is composed of different characters")
else:
    print("It has equal characters")