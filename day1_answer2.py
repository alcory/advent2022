#Same as before, 

with open('file.in') as file:
    data = [i for i in file.read().strip().split("\n")]

sum = 0
resultList = []
for i in data:
  if i != "":
    sum = sum + int(i)
  if i == "":
    resultList.append(sum)
    sum = 0

resultList.sort(reverse=True)

myresult = resultList[0] + resultList[1] + resultList[2]
print(myresult)
