list1 = ["A", "B", "C", "D"]
print(list1)
print(list1[3])
print(f"list1 has {len(list1)} items.") #prints list size

##################################################################

list2 = ["Red", 17, False, "Python"]
print(list2[1:3]) # start index 1 and ends index 2. # index 3 is not included
print(list2[-2]) # - ile başladığında listenin sağından 2.yi ekrana bastırır


list2[3] = 6 # replace list item with new item
list2.append("Apple") # Change last item
list2.insert(3, True) # Insert (index, object)
list2.remove("Red")
print(list2)

for i in list2:
  print(i)

if 20 in list2:
  print("Found!")
else:
  print("Not Found. :(")

list3 = list2.copy()
print(list3)
