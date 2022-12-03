#This allows us to transform the data, from a webpage with diferent lines to a list where the whitespace lines are also a list item
with open('file.in') as file:
    data = [i for i in file.read().strip().split("\n")]

#We create to variables, one is a counter and the other is for storage. Every time the iteration finds a number, its summed to the counter.When a space is found,
#the storage's value is compared to the counter. If the counter is higher, the storage is set to the counter's value. At the end of every iteration, the counter is set
#to 0 again. #At the end of the loop, the highest value found will be stored in totalSum.
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
