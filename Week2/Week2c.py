tuple1 = ("A", "B", "C", "D")
print(tuple1)
# tuple1[0] = "X"

list1 = list(tuple1)
list1[0] = "X"
tuple1 = tuple(list1)
print(tuple1)

i = 0
while i < len(tuple1):
  print(tuple1[i])
  i += 1

print("Done.") 

for x in range(5):
  print(x)
print("Done")