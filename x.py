numbers = [66, 78, 2, 45, 97, 17, 34, 105, 44, 52]
i = len(numbers)
print(len(numbers))
newList = []

while (i > 0):
  newList.append(numbers[i-1])
  i -= 1

print(newList)