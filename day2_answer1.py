with open('.\day2\day2_DATA.in') as file:
    data = [i for i in file.read().strip().split("\n")]



#For loop where we append every possible combination of results. The value's correspond
# to the given instructions
listOfResults = []
for i in data:
    if i[0] == 'A':
        if i[2] == 'Y':
            listOfResults.append(8) #Paper (+2) + Win (+6)
        if i[2] == 'X':
            listOfResults.append(4) #Rock (+1) + Draw (+3)
        if i[2] == 'Z':
            listOfResults.append(3) #Scissors (+3) + Loose (+0)
    if i[0] == 'B':
        if i[2] == 'Y':
            listOfResults.append(5) #Paper (+2) + Draw (+3)
        if i[2] == 'X':
            listOfResults.append(1) #Rock (+1) + Loose (+0)
        if i[2] == 'Z':
            listOfResults.append(9) #Scissors (+3) + Win (+6)
    if i[0] == 'C':
        if i[2] == 'Y':
            listOfResults.append(2) #Paper (+2) + Loose (+0)
        if i[2] == 'X':
            listOfResults.append(7) #Rock (+1) + Win (+6)
        if i[2] == 'Z':
            listOfResults.append(6) #Scissors (+3) + Draw (+3)

#Finally, all elements are summed together
defSum = sum(listOfResults)
print("def sum is:", defSum)
