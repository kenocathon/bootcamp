# Create two separate lists with 5 numbers
list_1 = [12,23,18,99,46]
list_2 = [44,38,67,44,29]

# Create two other lists called “squares” and “cubes”
squares = []
cubes = []

# Fill the first one with the squares of the values from the first list, and # # the second with the cubes, respectively.
for i in list_1:
  num_squared = i ** 2
  squares.append(num_squared)

for i in list_1:
  num_cubed = i ** 2
  cubes.append(num_cubed)

# Create another list called “biglist” which is the composite of the squares # # and cubes.
biglist = squares + cubes

# Print out all the values from the big list. If the value is an odd number, # # print out “is an odd number”, and if it’s even, print “is an even number”.
for x in biglist: 
      
    if x % 2 != 0: 
        x = str(x)
        print(x + ' is an odd number') 
for n in biglist:
    if n % 2 == 0:
        n = str(n)
        print(n + ' is an even number')