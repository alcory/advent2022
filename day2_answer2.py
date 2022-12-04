with open('.\day2\day2_DATA.in') as file:
    data = [i for i in file.read().strip().split("\n")]



#For loop where we append every possible combination of results. The value's correspond to the given instructions
#Y means you need to draw (+3 points), X means you need to loose (+0 points), Z means you need to win (+6 points). Depending on the value of the
#i[0], you will need one or another result. Remember that Rock (+1point), Paper (+2points), Scissor (+3points)
listOfResults = []
for i in data:
    if i[0] == 'A':
        if i[2] == 'Y':
            listOfResults.append(4) #Draw (+3) + Rock (+1)
        if i[2] == 'X':
            listOfResults.append(3) #Loose (+0) + Scissors (+3)
        if i[2] == 'Z':
            listOfResults.append(8) #Win (+6) + Paper (+2)
    if i[0] == 'B':
        if i[2] == 'Y':
            listOfResults.append(5) #Draw (+3) + Paper (+2)
        if i[2] == 'X':
            listOfResults.append(1) #Loose (+0) + Rock (+1)
        if i[2] == 'Z':
            listOfResults.append(9) #Win (+6) + Scissors (+3)
    if i[0] == 'C':
        if i[2] == 'Y':
            listOfResults.append(6) #Draw (+3) + Scissors (+3)
        if i[2] == 'X':
            listOfResults.append(2) #Loose (+0) + Paper (+2)
        if i[2] == 'Z':
            listOfResults.append(7) #Win (+6) + Rock (+1)

#Finally, all elements are summed together
defSum = sum(listOfResults)
print("def sum is:", defSum)