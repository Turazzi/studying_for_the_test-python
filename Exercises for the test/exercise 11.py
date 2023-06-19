#The function returns True if s2 is contained in s1. For example, if s1 = 'abdef' and s2 = 'def', the function should return True

def conteined_list(s1, s2):

    if len(s2) > len(s1):
        return False

    i = 0
    j = 0
    contained = False
    while i < len(s1) and j < len(s2) and len(s1) - i >= len(s2) - j:
        if s1[i] == s2[j]:
            contained = True
            j += 1
        else:
            contained = False
            j = 0
        i += 1
    return contained

s1 = input("Enter a word: ")
s2 = input("Enter another word: ")

print(conteined_list(s1, s2))