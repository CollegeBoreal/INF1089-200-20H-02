
# List
l = [ 1, 2, 3, 5, 1, 3, 10, 4 ]
l = [ x for x in range(200) if x % 2 == 0 and x <= 10 ]
print(l)

# Set
# s = { 1, 2, 3, 4, 5, 10 }
s = { x for x in range(200) if x % 2 == 0 and x <= 10 }
print(s)

# Dictionaire
#d = { 0: 2, 2: 4, 4: 8, 6: 12}
d = { x: x * 2 for x in range(200) if x % 2 == 0 and x <= 10 }
print(d)
