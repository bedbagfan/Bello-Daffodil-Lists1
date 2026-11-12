list = ["Notebook","Pen","Calculator","Laptop","Book"]
print("Original List: ", (', '.join(list)))
a = int(input("Input Index to Update: "))
b = input("Input New Value: ")
c = int(input("Enter Slice Range 1: "))
d = int(input("Enter Slice Range 2: "))
s = input("Enter Search item: ")

print(f"\nIndex to Update: {a}")
print(f"New Value: {b}")

slice = list[c:d]
print(f"Sliced List: ({c}:{d}) {', '.join(slice)}")
if s in slice:
  sr = f"{s} is found in the sliced list"
else:
  sr = f"{s} is not found in the sliced list"
print("Search Result (from sliced array):", sr)

list[a] = b
print(f"Updated List: {', '.join(list)}")
