
thing1 = [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1 ]
# attempting thing in octal
thing = [ 1, 1, 1, 1, 0, 1 ]

# Convert from a given base number system to decimal
sum = 0
invert = 0
base = 2 
for i in range((len(thing) - 1), -1, -1):
    radix = base**invert
    digit = thing[i]
    sum = sum + (radix * digit)
    invert = invert + 1

print(sum)
