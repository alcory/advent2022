with open('file.in') as file:
    data = [i for i in file.read().strip().split("\n")]

sum = 0
totalSum = 0
for i in data:
  if i != "":
    sum = sum + int(i)
  if i == "":
    if sum > totalSum:
      totalSum = sum
    sum = 0
      
print(totalSum)