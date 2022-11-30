def nonrepeat(string):
    freq = {}   #dict

    for x in string: #Traversing through string
        freq[x] = freq.get(x,0) + 1 

    for i in string:
        if freq[i] == 1:
            return i

    return -1

print(nonrepeat('abcddabceeff '))

#     else:

# print('This char dosent have any repeat char')