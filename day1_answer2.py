#Same as before, this allows us to transform the data, from a webpage with diferent lines to a list where the whitespace lines are also a list item

with open('file.in') as file:
    data = [i for i in file.read().strip().split("\n")]

#We create two variables: a counter an a list. On every iteration, if the value iterated is a non-space value, it is summed to the counter. On the other hand,
#if the value found is a whitespace, the counter's value is appended to the list and the counter's value is set to 0 to the next iteration. At the end of the for loop,
#resulList will contain a list of the sum of each elf's calories.
sum = 0
resultList = []
for i in data:
  if i != "":
    sum = sum + int(i)
  if i == "":
    resultList.append(sum)
    sum = 0

#Now the list is sorted in reverse order, from the highest number to the lowest. The three first values will be the highsest of the list.
resultList.sort(reverse=True)

myresult = resultList[0] + resultList[1] + resultList[2]
print(myresult)
