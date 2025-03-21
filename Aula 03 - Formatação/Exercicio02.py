x = True
y = False

print(f"a: {x and y}")
print(f"b: {x or y}")
print(f"c: {x and y or x}")
print(f"d: {x or y or x}")
print(f"e: {not (x or not y)}")
print(f"f: {not (not x and not y)}")
print(f"g: {not (not x and not y)}")
print(f"h: {not x and y}")
print(f"i: {not (x and y)}")
print(f"j: {not x and y or x}")
print(f"k: {not (x and y)and y}")
print(f"l: {x and y or y and not x}")
print(f"m: {not (x or y and y or y)}")