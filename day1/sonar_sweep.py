# opens a file in read mode

# file object = open(file_name [, access_mode][, buffering])
dataFile = open('input.txt', 'r')

# print the file
# print(dataFile.read().splitlines()) -> returns array os strings

# list of strings from the dataFile, map must take two arguments: type, array
# converting strings into integers
depths = list(map(int, dataFile.read().splitlines()))
# print(depths) -> array of ints

larger_measurements = 0

for i in range(len(depths)): #len(depths) === 10
    if depths[i] > depths[i - 1]:
      larger_measurements = larger_measurements + 1

print(larger_measurements)
dataFile.close() # good practice to close a file
